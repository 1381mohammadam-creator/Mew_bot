import http.server
import os
import threading
import time
import urllib.request

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")


# این بخش یک سرور الکی روشن می‌کنه تا رندر فکر کنه سایت داریم و خاموشش نکنه
class SimpleHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    self.wfile.write(b"Bot is alive!")


def run_server():
  server = http.server.HTTPServer(("0.0.0.0", 10000), SimpleHandler)
  server.serve_forever()


# سرور رو توی پس‌زمینه روشن می‌کنیم
threading.Thread(target=run_server, daemon=True).start()


# تابع فرستادن پیام میو
def send_meow():
  if not TOKEN or not CHAT_ID:
    print("خطا: توکن یا آیدی گروه تنظیم نشده است!")
    return

  url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
  data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": "میو"}).encode(
      "utf-8"
  )

  try:
    req = urllib.request.Request(url, data=data)
    urllib.request.urlopen(req)
    print("پیام 'میو' با موفقیت ارسال شد!")
  except Exception as e:
    print(f"خطا در ارسال: {e}")


print("ربات روشن شد...")

# حلقه ۵ دقیقه یک بار
while True:
  send_meow()
  time.sleep(300)
