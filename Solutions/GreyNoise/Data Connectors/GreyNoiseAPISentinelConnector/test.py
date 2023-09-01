import json
from stixGen import GreyNoiseStixGenerator

def test_generate_indicator():
    gnIndicator = json.loads(r"""{"ip": "141.164.176.74","metadata": {"asn": "AS25019","city": "Ta’if","country": "Saudi Arabia","country_code": "SA","organization": "Saudi Telecom Company JSC",
"category": "isp","tor": false,"rdns": "" ,"os": "Windows 7/8","sensor_count": 78,"sensor_hits": 433,"region": "Mecca Region",
"destination_countries": ["Belarus","United States","Saudi Arabia","Bulgaria","United Kingdom","Israel",
"Australia",
        "Indonesia",
        "South Korea"
      ],
      "source_country": "Saudi Arabia",
      "source_country_code": "SA",
      "destination_country_codes": [
        "BY",
        "US",
        "SA",
        "BG",
        "GB",
        "IL",
        "AU",
        "ID",
        "KR"
      ]
    },
    "bot": false,
    "vpn": false,
    "vpn_service": "N/A",
    "spoofable": false,
    "raw_data": {
      "scan": [
        {
          "port": 445,
          "protocol": "TCP"
        },
        {
          "port": 1433,
          "protocol": "TCP"
        }
      ],
      "web": {},
      "ja3": [],
      "hassh": []
    },
    "first_seen": "2023-08-23",
    "last_seen": "2023-08-25",
    "seen": true,
    "tags": [
      "MSSQL Bruteforcer",
      "SMBv1 Crawler"
    ],
    "actor": "unknown",
    "classification": "malicious",
    "cve": []
    }""")

    stixGen = GreyNoiseStixGenerator()
    indicator = stixGen.generate_indicator(gnIndicator)
    print(indicator)

if __name__ == "__main__":
    test_generate_indicator()