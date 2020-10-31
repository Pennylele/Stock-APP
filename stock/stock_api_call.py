from datetime import date, datetime, timedelta
import requests

def stock_api_call(ticker):
    # adding 5 days
    def adding_5_days(ticker):
        time_container = []
        unix_container = []
        json_container = []
        time_label = []
        fmt = '%Y-%m-%d'
        now = datetime.today()
        start = datetime(now.year, now.month, now.day, 20, 00) - timedelta(days=1)
        while len(time_container) < 6:
            if start.weekday() < 5:
                time_container.insert(0, start)
                # adding dates to labels
                time_label.insert(0, start.strftime(fmt))
            start = start - timedelta(days=1)
        # converting the datetime into UNIX
        for i in time_container:
            unix_container += [int(datetime.timestamp(i))]
        # calling the API
        for j in unix_container:
            r = requests.get('https://finnhub.io/api/v1/stock/candle?symbol='+ticker+'&resolution=1&from='+str(j)+'&to='+str(j)+'&token=bt632u748v6vp4gago5g')
            json_container += [r.json()]
        return json_container, time_label

    def stock_prices(ticker):
        dic = {}
        prices = []
        labels=[]
        data = adding_5_days(ticker)
        days = data[0]
        time_label = data[1]
        for l in days:
            try:
                prices += [l["c"][0]]
                v = time_label[days.index(l)]
                labels.append(v)
                dic[v] = l["c"][0]
            except:
                print("Oops")
        return prices, labels, dic

        # find the maximum profit
    def maxPri(ticker):
        data = stock_prices(ticker)
        store = []
        prices = data[0]
        labels = data[1]
        dic = data[2]
        if not prices:
            print("No prices")
        else:
            minPri, maxPri = prices[0], 0
            for i in range(1, len(prices)):
                minPri = min(minPri, prices[i])
                store.append([prices[i], minPri])
                maxPri = max(prices[i]-minPri, maxPri)
            return store, prices, dic, maxPri, labels

    results = {}
    data = maxPri(ticker)
    store = data[0]
    price = data[1]
    dic = data[2]
    maxPri_rounded =round(data[3], 2)
    labels = data[4]

    for i in store:
        if i[0] - i[1] == data[3]:
            results['buy'] = i[1]
            results['sell'] = i[0]

    key_list = list(dic.keys())
    val_list = list(dic.values())   
    buy_date = key_list[val_list.index(results['buy'])]
    sell_date = key_list[val_list.index(results['sell'])]
    results['buy_date'] = buy_date
    results['sell_date'] = sell_date
    results['maxPri'] = maxPri_rounded
    results['prices'] = price
    results['labels'] = labels
        
    return results

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    stock_api_call(arg)

