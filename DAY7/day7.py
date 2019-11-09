#* Một file csv chứa danh sách các mặt hàng đã được bán ra của một cửa hàng trong ngày,
#* mỗi dòng là thông tin về một lần khách mua hàng, bao gồm mã hàng hóa, 
#* số lượng hàng hóa bán ra, giá bán ra, giá gốc nhập về. Các dòng khác nhau có thể có 
#* cùng mã hàng hóa (nhiều người mua cùng 1 mặt hàng). Viết chương trình tạo ra file csv
#* trong đó mỗi dòng chứa thông tin về tình trạng kinh doanh của một mặt hàng, gồm các cột : 
#* mã hàng hóa (chỉ tính một lần duy nhất cho các lần mua khác nhau của cùng một mặt hàng),
#* tổng số lượng đã bán, tổng doanh số (số tiền thu được do bán hàng), tổng lợi nhuận (số tiền thu được sau khi trừ đi giá gốc nhập về).
#* Các mặt hàng xếp theo trình tự giảm dần của doanh số. Ví dụ :
#* File input.csv:
#* MaSP,SoLuong,GiaBan,GiaNhap
#* VINAMILK01, 5, 27000, 20000
#* THMILK03, 10, 28000, 20000
#* OMACHI05, 2, 6000, 4000
#* VINAMILK01, 5, 27000, 20000
#* VINAMILK01, 10, 27000, 20000
#* OMACHI05, 5, 6000, 4000
#* File output.csv:
#* MaSP,SoLuong,DoanhSo,LoiNhuan
#* VINAMILK01, 20, 540000, 140000
#* THMILK03, 10, 280000, 80000
#* OMACHI05, 7, 42000, 14000

import csv
#*******************************

#*******************************
#****** Function
def pr(content_print):
    print(content_print)
# ---------------------------------
def write_file_csv(path_save_file,col_csv,row_csv):
    with open(path_save_file,'w+') as file:
        fidldnames = ['column1','column2','column3']
        thewriter = csv.DictWriter(file,fieldnames=fidldnames)
        thewriter.writerow(['col1','col2','col3'])
        for i in range(1,100):
            thewriter.writerow('one','two','three')
def filter_row(data_filter,content_row,colunm):
    newdata = list()
    for line in data_filter:
        if content_row in line[colunm]:
            newdata.append(line)
    return newdata
# ************* Main *************
def main():
    header_output = ['MaSP','SoLuong','DoanhSo','LoiNhuan']
    result = list()
    with open('data.csv','r') as csvdata:
        csv_reader = csv.DictReader(csvdata)

        with open('output.csv','w') as newfile:
            write_csv = csv.DictWriter(newfile,fieldnames=header_output,delimiter='\t')
            write_csv.writeheader()
            

            for line in filter_row(csv_reader,'VINAMILK01','MaSP'):
                pr(line['SoLuong'])










main()



