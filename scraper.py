import requests
import pandas as pd
import json

cookies = {
    'TAUnique': '%1%enc%3A%2B3ZCtJxTIBQkW7Qodlo6EssIq2GHqYmduQSnw4ELBBwxa2ZqnAW%2FKJs8F9ZmyiAuNox8JbUSTxk%3D',
    'TADCID': 'whlL94K3rJe9ZyalABQCrj-Ib21-TgWwDB4AzTFpg4J-5DO8DGqA3A21TAmg4XRsWYukvWyla6OuYN_qrtMCFczPtvX8_uNC848',
    'TASameSite': '1',
    'TASSK': 'enc%3AAP8heOVLz6wzg%2BJszYISmubB1suaXaTbMYEC%2Fo4iEFEwZuMJ%2FkEDsTtxah7VrdEr8A0tsd9nqPuV%2FAI0TD44gwAKcl2laWvrx%2FEo5rSoPdUQudf3zw15QrXovNFglYvqCA%3D%3D',
    'TART': '%1%enc%3AVc3vMjpqeUMpNMWkVtMRMxr0ad5qgfavRndwlEwhOcfa3ezTjD47jz8cGfhoJavIlxPw837%2Frn8%3D',
    'VRMCID': '%1%V1*id.10568*llp.%2F*e.1735748642061',
    'TATrkConsent': 'eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9',
    'ServerPool': 'B',
    'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*RS.1',
    '__vt': 'Kipnpzpf12KcyaSYABQCjdMFtf3dS_auw5cMBDN7STJgcYuiq8jzjseuo0YpwWrIm6cJpukMLdp89tcpTpysGpMmHFnPwKQ7K-MGbpVNIF64eeoBqNBIC1t-ueU1OJQHVbJZe0r6UALMJvByAKIWWkHU0g',
    'PAC': 'AJ96KSfYqAyde9K4wPLiEZyMRGzFrIlYTMO9X5vwBY9nDoyNsl7hoA_ZTmZruZh90pCVW5N9Ta6DDQas3q_Iyc_-LAnCYAvGI0iOSCHP7mYhAQE6cb3lEZJxafcKw0vZ5NvzGxL3xTPyc5ZkkWqzaO0yG9OvJ93ZqnGNu1Ox5SGcy92B7aSyc_JVM0yWBfTPtQ%3D%3D',
    'SRT': 'TART_SYNC',
    'PMC': 'V2*MS.8*MD.20241225*LD.20241226',
    'TASID': 'F4A54BD1EC764CE4AE7E7F40A87D7CC4',
    'TAUD': 'LA-1735184947169-1*RDD-1-2024_12_25*LG-19239784-2.1.F.*LD-19239785-.....',
    'TASession': 'V2ID.F4A54BD1EC764CE4AE7E7F40A87D7CC4*SQ.10*LS.Hotels*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.1*EAU._',
    'datadome': 'X5S41bm08bO1IpcxEtwo_koUyfa5OHtgqpibuhr7udyO1hue4TXt_~L8wCWMhpePqHOnvJ_hRJq4ttSzm28h4HxNDe962TjV0Jnp3KEKa2uV79RFviJVSpdt__kXKogd',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Dec+26+2024+14%3A11%3A23+GMT%2B0500+(Pakistan+Standard+Time)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=49e3025e-ad7c-46de-a6c0-31d2a1702c37&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'TAUnique=%1%enc%3A%2B3ZCtJxTIBQkW7Qodlo6EssIq2GHqYmduQSnw4ELBBwxa2ZqnAW%2FKJs8F9ZmyiAuNox8JbUSTxk%3D; TADCID=whlL94K3rJe9ZyalABQCrj-Ib21-TgWwDB4AzTFpg4J-5DO8DGqA3A21TAmg4XRsWYukvWyla6OuYN_qrtMCFczPtvX8_uNC848; TASameSite=1; TASSK=enc%3AAP8heOVLz6wzg%2BJszYISmubB1suaXaTbMYEC%2Fo4iEFEwZuMJ%2FkEDsTtxah7VrdEr8A0tsd9nqPuV%2FAI0TD44gwAKcl2laWvrx%2FEo5rSoPdUQudf3zw15QrXovNFglYvqCA%3D%3D; TART=%1%enc%3AVc3vMjpqeUMpNMWkVtMRMxr0ad5qgfavRndwlEwhOcfa3ezTjD47jz8cGfhoJavIlxPw837%2Frn8%3D; VRMCID=%1%V1*id.10568*llp.%2F*e.1735748642061; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; ServerPool=B; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; __vt=Kipnpzpf12KcyaSYABQCjdMFtf3dS_auw5cMBDN7STJgcYuiq8jzjseuo0YpwWrIm6cJpukMLdp89tcpTpysGpMmHFnPwKQ7K-MGbpVNIF64eeoBqNBIC1t-ueU1OJQHVbJZe0r6UALMJvByAKIWWkHU0g; PAC=AJ96KSfYqAyde9K4wPLiEZyMRGzFrIlYTMO9X5vwBY9nDoyNsl7hoA_ZTmZruZh90pCVW5N9Ta6DDQas3q_Iyc_-LAnCYAvGI0iOSCHP7mYhAQE6cb3lEZJxafcKw0vZ5NvzGxL3xTPyc5ZkkWqzaO0yG9OvJ93ZqnGNu1Ox5SGcy92B7aSyc_JVM0yWBfTPtQ%3D%3D; SRT=TART_SYNC; PMC=V2*MS.8*MD.20241225*LD.20241226; TASID=F4A54BD1EC764CE4AE7E7F40A87D7CC4; TAUD=LA-1735184947169-1*RDD-1-2024_12_25*LG-19239784-2.1.F.*LD-19239785-.....; TASession=V2ID.F4A54BD1EC764CE4AE7E7F40A87D7CC4*SQ.10*LS.Hotels*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.1*EAU._; datadome=X5S41bm08bO1IpcxEtwo_koUyfa5OHtgqpibuhr7udyO1hue4TXt_~L8wCWMhpePqHOnvJ_hRJq4ttSzm28h4HxNDe962TjV0Jnp3KEKa2uV79RFviJVSpdt__kXKogd; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+26+2024+14%3A11%3A23+GMT%2B0500+(Pakistan+Standard+Time)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=49e3025e-ad7c-46de-a6c0-31d2a1702c37&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'origin': 'https://www.tripadvisor.com',
    'priority': 'u=1, i',
    'referer': 'https://www.tripadvisor.com/Search?q=hotels+in+New+York&geo=1&ssrc=a&searchNearby=false&searchSessionId=0012189272dd0a03.ssid&offset=0',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.205", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


def get_all_data(keyword, query, location_id, off_se):
    json_data = [
        {
            'variables': {
                'request': {
                    'filters': {
                        'dataTypes': [
                            'LOCATION',
                        ],
                        'locationTypes': [
                            keyword.upper(),
                        ],
                    },
                    'locale': 'en-US',
                    'query': query.lower(),
                    'offset': off_se,
                    'scope': {
                        'locationId': location_id,
                        'center': None,
                    },
                    'locationIdsToExclude': [],
                    'categoryFilterIds': [
                        'HOTELS',
                        'ATTRACTIONS',
                        'RESTAURANTS',
                        'VACATION_RENTALS',
                    ],
                    'additionalFields': [
                        'SNIPPET',
                        'MENTION_COUNT',
                    ],
                    'limit': 30,
                },
            },
            'extensions': {
                'preRegisteredQueryId': 'd65d51b7e2ed4f40',
            },
        },
    ]
    response = requests.post('https://www.tripadvisor.com/data/graphql/ids', cookies=cookies, headers=headers, json=json_data)
    # data = '[{"variables":{"request":{"filters":{"dataTypes":["LOCATION"],"locationTypes":[query]},"locale":"en-US","query":"restaurants","offset":30,"scope":{"locationId":60763,"center":null},"locationIdsToExclude":[],"categoryFilterIds":["HOTELS","ATTRACTIONS","RESTAURANTS","VACATION_RENTALS"],"additionalFields":["SNIPPET","MENTION_COUNT"],"limit":30}},"extensions":{"preRegisteredQueryId":"d65d51b7e2ed4f40"}}]'
    # response = requests.post('https://www.tripadvisor.com/data/graphql/ids', cookies=cookies, headers=headers, data=data)
    json_response = response.json()

    hotels = []

    for item in json_response:
        data = item.get("data", {})
        search_results = data.get("SERP_getSearchResultsList", {})
        clusters = search_results.get("clusters", [])

        for cluster in clusters:
            sections = cluster.get("sections", [])

            for section in sections:
                if section.get("__typename") == "SERP_PagedSearchResultsSection":
                    results = section.get("results", [])

                    # Loop through results to extract hotel details
                    for hotel in results:
                        details = hotel.get("details", {})
                        default = details.get('defaultUrl')
                        if not default.startswith == "htt":
                            default = "https://www.tripadvisor.com" + default
                        hotels.append({
                            "Location ID": details.get("locationId"),
                            "Name": details.get("localizedName"),
                            "Rating": details.get('reviewSummary', {}).get("rating"),
                            "No of reviews": details.get('reviewSummary', {}).get("count"),
                            "Default URL": default,
                            "Image URL": details.get("thumbnail", {}).get("photoSizeDynamic", {}).get("urlTemplate"),
                            "Description": details.get("locationDescription"),

                        })
    return hotels


if __name__ == "__main__":
    print("General Information about keywords:- ")
    print("----------")
    print("If you're scraping hotels: Use ACCOMMODATION.")
    print("If you're scraping restaurants: Use EATERY.")
    print("If you're scraping tourist spots: Use ATTRACTION.")
    # print("If you're planning a trip and need flights: Use FLIGHT.")
    # print("If you're looking for rentals: Use VACATION_RENTAL.")
    print("----------\n")

    lo_cat = {
        "new york": 60763,
        "los angeles": 32655,
        "chicago": 35805,
        "paris": 187147,
        "london": 186338,
        "tokyo": 298184,
        "moscow": 213035,
        "istanbul": 28763,
        "berlin": 103105,
        "rome": 165846,
        "dubai": 24956,
        "barcelona": 174275,
        "sydney": 107248,
        "singapore": 29491,
        "bangkok": 111019,
        "san francisco": 29372,
        "amsterdam": 16986,
        "las vegas": 47425,
        "vienna": 137514,
        "madrid": 186195,
        "cairo": 195870,
        "lagos": 194362,
        "hong kong": 296451,
        "seoul": 28227,
        "mexico city": 122350,
        "cape town": 188015,
        "kuala lumpur": 29491,
        "mumbai": 24353,
        "buenos aires": 19975,
        "jakarta": 297378,
        "lima": 174850,
        "sao Paulo": 185176,
    }

    # print(f"Some predefined locations: {lo_cat}")

    print(f"Available locations: {', '.join(lo_cat.keys())}")
    location_name = input("Enter the name of the location: ").strip()
    loc = lo_cat.get(location_name.lower())

    if not loc:
        print(f"Error: '{location_name}' is not a valid location. Please choose from {', '.join(lo_cat.keys())}.")
        print("-------------------------------")
        print("If any location is not present simple add it to the lo_cat dictionary.")
        exit()

    que = input("Please enter what you want to scrape from TripAdvisor (Your Query): ").strip()
    keyw = input("Please enter the keyword: ").strip()

    main_data = []
    i = 0
    while True:
        try:
            print(f"Scraping data from page {i}...")
            data = get_all_data(keyword=keyw, query=que, location_id=loc, off_se=i * 30)
            if data:
                print(f"Successfully scraped data from page {i}")
                main_data.extend(data)
            else:
                print("No more data to scrape.")
                break
        except Exception as e:
            print(f"Error encountered. No more json data present!")
            break
        i += 1

    if main_data:
        df = pd.DataFrame(main_data)
        df.to_csv(f"tripadvisor_{que}_{location_name}.csv", index=False)
        df.to_excel(f"tripadvisor_{que}_{location_name}.xlsx", index=False)
        with open(f"tripadvisor_{que}_{location_name}.json", 'w', encoding='utf-8') as file:
            json.dump(main_data, file, ensure_ascii=False, indent=4)
        print(
            f"Extracted {len(main_data)} {que}. Saved as 'tripadvisor_{que}_{location_name}.csv', 'tripadvisor_{que}_{location_name}.xlsx' and tripadvisor_{que}_{location_name}.json")
    else:
        print("No data extracted.")
