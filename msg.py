import data


def time(ttime):
    ttime = ttime.split("T")[0] + " " + ttime.split("T")[1]
    return ttime.split(".")[0]


def construct_message(message):
    try:
        dt = data.getData(data.convert_name(message.text))
        dt['rate'] = "{:.3f}".format(dt["rate"])
        name = "«"+message.text+"»"
        msg = f"*****{time(dt['src_side_base'][0]['time'])}*****\n" \
              f"{name}\n" \
              f"1 {dt['asset_id_base']} = {dt['rate']}$"
    except Exception as ex:
        # print(ex)
        msg = f"Валюта {message.text} не найдена"

    return msg
