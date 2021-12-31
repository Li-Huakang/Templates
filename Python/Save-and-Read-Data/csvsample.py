import csv
# save as csv
with open(writename, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 先写入columns_name
    writer.writerow(["Vds","Ids"])
    for key in res:
        # print(key)
        writer.writerow(["Vgs = "+str(key)])
        #写入多行用writerows
        writer.writerows(res[key])
# os.system("subl "+ writename)