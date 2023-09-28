"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Veronika Fellnerova
email: veronika.fellnerova@seznam.cz
discord: Verca F.#5057
"""

import requests
from bs4 import BeautifulSoup
import re
import sys
import csv


def take_numbers(input_string):
    if re.search(r"[^0-9]", input_string):
        clean_string = re.sub(r"[^0-9]", "", input_string)
        return clean_string
    else:
        return input_string


def validate_user_inputs(user_arguments: list[str]):
    # user has to send 2 args
    if len(user_arguments) != 2:
        raise ValueError("incorrect arguments")
    # url validation
    try:
        response = requests.get(user_arguments[0])
        soup = BeautifulSoup(response.text, features="html.parser")
        title = soup.h1.get_text().strip()
    except:
        raise ValueError("url argument cannot be used")
    if (
        title
        != "Volby do Poslanecké sněmovny Parlamentu České republiky konané ve dnech 20.10. – 21.10.2017 (promítnuto usnesení NSS)"
    ):
        raise ValueError("wrong url sent")
    # file name validation
    ext = (user_arguments[1].split("."))[1]
    if ext != "csv":
        raise ValueError("file must be csv")


validate_user_inputs(sys.argv[1:])

user_input_url = sys.argv[1]
user_input_filename = sys.argv[2]


response = requests.get(user_input_url)

soup = BeautifulSoup(response.text, features="html.parser")


nazev_obce_class_selector = "overflow_name"
url_obce_class_selector = "center"
kod_obce_class_selector = "cislo"

obce_url_list = []
url_http = "https://volby.cz/pls/ps2017nss/"

for tr in soup.select("table tr"):
    obce_url_item = {}

    kod_obce_element = tr.find(class_=kod_obce_class_selector)
    if kod_obce_element is not None:
        obce_url_item["kod"] = kod_obce_element.get_text()

    obec_element = tr.find(class_=nazev_obce_class_selector)
    if obec_element is not None:
        obce_url_item["nazev"] = obec_element.get_text()

    url_element = tr.find(class_=url_obce_class_selector)
    if url_element is not None:
        url_tag = url_element.find("a")
        if url_tag is not None:
            obce_url_item["url"] = url_http + url_tag.get("href")

    obce_url_list.append(obce_url_item)

obce_url_list = list(filter(None, obce_url_list))


list_vysledky_obce = []

for obec_element in obce_url_list:
    response = requests.get(obec_element["url"])

    volici_v_seznamu_obec_1_okresk_selector = "#ps311_t1 td:nth-child(4)"

    soup = BeautifulSoup(response.text, features="html.parser")

    okrsek_odkazy = []

    if soup.find(attrs={"id": "s1"}):
        # vice okrsku
        for okrsek in soup.find_all(class_="cislo"):
            okrsek_element = okrsek.find("a")
            okrsek_odkazy.append(url_http + okrsek_element.get("href"))
        output_dict = {
            "code": obec_element["kod"],
            "location": obec_element["nazev"],
            "registered": 0,
            "envelopes": 0,
            "valid": 0,
        }
        for okrsek_odkaz in okrsek_odkazy:
            okrsek_response = requests.get(okrsek_odkaz)
            okrsek_soup = BeautifulSoup(okrsek_response.text, features="html.parser")
            registered = int(
                take_numbers(
                    okrsek_soup.select_one("table tr:nth-child(2) td:nth-child(1)").text
                )
            )
            envelopes = int(
                take_numbers(
                    okrsek_soup.select_one("table tr:nth-child(2) td:nth-child(2)").text
                )
            )
            valid = int(
                take_numbers(
                    okrsek_soup.select_one("table tr:nth-child(2) td:nth-child(5)").text
                )
            )
            output_dict["registered"] = output_dict["registered"] + registered
            output_dict["envelopes"] = output_dict["envelopes"] + envelopes
            output_dict["valid"] = output_dict["valid"] + valid

            for row in okrsek_soup.select(".t2_470 table tr"):
                y = row.select_one(".t2_470 table tr td:nth-child(2)")
                nazev_strany = ""
                if y is not None:
                    if y.text != "-":
                        nazev_strany = y.text
                celkem = row.select_one(".t2_470 table tr td:nth-child(3)")
                celkem_hlasu = 0
                if celkem is not None:
                    if celkem.text != "-":
                        celkem_hlasu = take_numbers(celkem.text)
                        celkem_hlasu = take_numbers(celkem.text)
                        celkem_hlasu = take_numbers(celkem.text)

                if nazev_strany not in output_dict:
                    output_dict[nazev_strany] = celkem_hlasu
                else:
                    output_dict[nazev_strany] = int(output_dict[nazev_strany]) + int(
                        celkem_hlasu
                    )

        output_dict = {
            key: value for key, value in output_dict.items() if key != ""
        }  # delete empty items in dict

        list_vysledky_obce.append(output_dict)

    else:
        # 1 okrsek
        output_dict = {
            "code": obec_element["kod"],
            "location": obec_element["nazev"],
            "registered": take_numbers(
                soup.select_one("#ps311_t1 td:nth-child(4)").text
            ),
            "envelopes": take_numbers(
                soup.select_one("#ps311_t1 td:nth-child(5)").text
            ),
            "valid": take_numbers(soup.select_one("#ps311_t1 td:nth-child(8)").text),
        }

        for row in soup.select(".t2_470 table tr"):
            y = row.select_one(".t2_470 table tr td:nth-child(2)")
            nazev_strany = ""
            if y is not None:
                if y.text != "-":
                    nazev_strany = y.text
            celkem = row.select_one(".t2_470 table tr td:nth-child(3)")
            celkem_hlasu = 0
            if celkem is not None:
                if celkem.text != "-":
                    celkem_hlasu = take_numbers(celkem.text)
            output_dict[nazev_strany] = celkem_hlasu

        output_dict = {
            key: value for key, value in output_dict.items() if key != ""
        }  # delete empty items in dict
        list_vysledky_obce.append(output_dict)


# Write to csv
csv_headers = list_vysledky_obce[0].keys()

with open(user_input_filename, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    writer.writeheader()

    for vysledek_obce in list_vysledky_obce:
        row_data = {csv_header: vysledek_obce[csv_header] for csv_header in csv_headers}
        writer.writerow(row_data)
