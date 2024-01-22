
class Library:
    def __init__(self):
        self.book_list = []
        self.book_list_InLibrary = []
        self.rental_list = [[] ,[] ,[]]
        self.rant_num = 0 #빌려준 횟수 대여 id 처럼 사용

    def buy_book(self,book_name):
        self.book_list.append(book_name)
        self.book_list_InLibrary.append(book_name)

    def rant_book(self,book_name, client_name):
        if self.book_list_InLibrary.count(book_name) != 0:
            self.rental_list[0].append(book_name)
            self.rental_list[1].append(client_name)
            self.rental_list[2].append(self.rant_num)
            self.rant_num += 1
            self.book_list_InLibrary.remove(book_name)
            print("대여 완료 대여만료일은 대여일부터 7일 까지입니다.")

        elif self.book_list.count(book_name) != 0:
            print("해당책은 이미 대여된 상태입니다.")

        else:
            print("해당책은 도서관에 존재하지 않습니다.")


    def book_info_InLibrary(self):
        print("현재 도서관 안에 있는 책목록은 다음과 같습니다.",self.book_list_InLibrary)
        
    def retrun_book(self, number, book_name, client_name):
        if self.rental_list[2].count(number) != 0:
            i = self.rental_list[2].index(number)
            if self.rental_list[0][i] == book_name and self.rental_list[1][i] == client_name:
                del(self.rental_list[:][i])
                self.book_list_InLibrary.append(book_name)
                print("도서반납이 완료되었습니다. 감사합니다.")
            else:
                print("대출기록과 일치하지 않는 정보입니다. 다시 시도해주세요")
        else:
            print("잘못된 id 입력")
        

def main():
    L1 = Library()
    L1.buy_book("book1")
    L1.buy_book("book2")
    L1.buy_book("book3")
    L1.rant_book("book1","noma")
    L1.rant_book("book1","noma")
    L1.rant_book("NOdata_book","noma")
    L1.book_info_InLibrary()
    L1.retrun_book(0,"book1","noma")
    L1.book_info_InLibrary()


if __name__ == "__main__":
    main()

