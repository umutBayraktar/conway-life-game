from Area import Area


def parse_input(input_string):

    if input_string == '' or input_string is None:
        print('Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')
        return None

    if ',' in input_string:
        parsed_input=input_string.split(',')
        if len(parsed_input) != 2:
            print('Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')
            return None
        else: #len == 2 x,y
            try:
                x = int(parsed_input[0])
                y = int(parsed_input[1])
                if x < 0 or y < 0:
                    print('İndis değeri negatif olamaz')
                    return None
                elif x > 7 or y > 7:
                    print('İndis değeri 7 den büyük olamaz')
                    return None
                else:
                    return {'x': x ,'y': y}
            except:
                print('Lütfen nümerik veri giriniz')
                return None
    else:
        print('Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz')
        return None



def loop_input(input_string):

    if input_string == '' or input_string is None:
        print("Yanlış girdi,lütfen 1 ve ya 2 giriniz")
        return -1

    try:
        number = int(input_string)
        if number is 1 or number is 2:
            return number
        else:
            print("Yanlış girdi,lütfen 1 ve ya 2 giriniz")
            return -1
    except:
        print("Yanlış girdi,lütfen 1 ve ya 2 giriniz")
        return -1


def positive_int_input(input_string):

    if input_string == '' or input_string is None:
        return None
    try:
        number = int(input_string)
        if number > 0:
            return number
        else:
            return None
    except:
        return None

#-------------------------------------------------------------------------------

print("Canway'in Hayat Oyunu\n")
print("8 x 8 lik bir alan için başlangıçta hayatta olan canlıların\n"
      "x,y şekinde indis bilgilerini giriniz.\n"
      "Örneğin yatayda 2 düşeyde 3 indisindeki canlı için 2,2")
inputs = []
while True:
    position = parse_input(input("Konum :"))
    if position is not None:
        if len(inputs) < 64:
            inputs.append(position)
            re_input = loop_input(input("Tekrar konum girmek için 1 , konum girme işlemini sonlandırmak için 2 giriniz: "))
            while re_input == -1:
                re_input = loop_input(input("Tekrar konum girmek için 1 , konum girme işlemini sonlandırmak için 2 giriniz: "))
            if re_input == 2:
                    break
        else:
            print("Maksimum girdi sayısına ulaşıldı")
            break


rep_count=positive_int_input(input("Oyun tekrar sayısını giriniz:"))
while(rep_count is None):
    rep_count = positive_int_input(input("Oyun tekrar sayısını giriniz:"))

game_area = Area(inputs)
for i in range(rep_count):

    print("{0}. oyun\n".format(i+1))
    print(game_area.print_area())
    game_area.update_cells()
    game_area.upgrade()
    print("------------------------\n\n")


