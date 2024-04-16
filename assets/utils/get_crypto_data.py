import requests
import json

# Định nghĩa điểm cuối API
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=20&convert=USD&CMC_PRO_API_KEY=004e068b-6866-4858-88ed-f954a28ba011"

# Gửi một yêu cầu GET đến API
response = requests.get(url)

# Phân tích phản hồi dưới dạng JSON
data = response.json()

# Khởi tạo một danh sách trống để lưu trữ các đối tượng
objects = []

# Lặp qua từng loại tiền điện tử trong dữ liệu
for crypto in data["data"]:
    # Tạo một đối tượng với các trường cần thiết
    obj = {
        "id": crypto["id"],
        "name": crypto["name"],
        "symbol": crypto["symbol"],
        "currency": "USD",
        "price": crypto["quote"]["USD"]["price"],
        "rank": crypto["cmc_rank"],
        "volume_24h": crypto["quote"]["USD"]["volume_24h"],
        "percent_change_24h": crypto["quote"]["USD"]["percent_change_24h"],
        "market_cap": crypto["quote"]["USD"]["market_cap"],
        "image": "https://s2.coinmarketcap.com/static/img/coins/64x64/" + str(crypto["id"]) + ".png"
    }
    # Thêm đối tượng vào danh sách
    objects.append(obj)

# Mở một file để ghi dữ liệu
with open('./assets/utils/crypto_data.json', 'w') as f:
    # Ghi dữ liệu vào file dưới dạng JSON
    json.dump(objects, f)

print("Dữ liệu đã được ghi thành công vào file 'crypto_data.json'")
