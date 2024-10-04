from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException

# কনফিগারেশন ফাইল থেকে ক্লায়েন্ট তৈরি করুন
client = GoogleAdsClient.load_from_storage("google-ads.yaml")

# একটি সিম্পল কুয়েরি চালান
def main(client):
    ga_service = client.get_service("GoogleAdsService")
    query = """
        SELECT campaign.id, campaign.name
        FROM campaign
        ORDER BY campaign.id
        LIMIT 10"""

    try:
        response = ga_service.search(customer_id="YOUR_CUSTOMER_ID", query=query)
        for row in response:
            print(f"Campaign with ID {row.campaign.id} and name {row.campaign.name} was found.")
    except GoogleAdsException as ex:
        print(f"Request with ID {ex.request_id} failed with status {ex.error.code().name}")
        print(f"Details: {ex.failure}")

if __name__ == "__main__":
    main(client)
