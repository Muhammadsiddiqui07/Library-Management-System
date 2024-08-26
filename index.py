import datetime

class LMS:
    def __init__(self):
        self.book = []
        self.bookReciver = [] 
    
    def add(self, title, author):
        print('-------------------------------------------------------------------------------------------------------')
        self.book.append({"Title": title, "Author": author})
        print('Your Library Has the Following Books:')        
        for book in self.book:
            print('Title:', book['Title'], ', Author:', book['Author'])
        self.lms()  

    def issue(self, name, contact, email):
        limit = 0
        print('-------------------------------------------------------------------------------------------------------')
        print("We have the following books. Please select accordingly ---> ")
    
        for book in self.book:
            print('Title:', book['Title'], ', Author:', book['Author'])
        
        print('-------------------------------------------------------------------------------------------------------')
    
        while limit < 3:
            print('Enter Title ---> ')
            title = input()
            print('Enter Author ---> ')
            author = input()            
            found = False
        
            for book in self.book:
                if book['Title'] == title and book['Author'] == author:
                    self.bookReciver.append({"Name": name, "Contact": contact, "Email": email, "Book Title": title, "Author": author})
                    self.book.remove(book)  
                    limit += 1
                    found = True
                    break
        
            if not found:
                print("Sorry, the book with the given title and author is not available.")
        
            if limit < 3:
                print(f"You can issue {3 - limit} more book(s).")
            else:
                print("You have reached the limit of 3 books.")
    
        print('----------Your Receipt------------')
    
        for issueBook in self.bookReciver:
            print('Name:', issueBook['Name'], '\n' +
                  'Contact:', issueBook['Contact'], '\n' +
                  'Email:', issueBook['Email'], '\n' +
                  'Title:', issueBook['Book Title'], '\n' +
                  'Author:', issueBook['Author'])         
    
        self.lms()

    def edit(self):
        print('-------------------------------------------------------------------------------------------------------')
        print("We have the following books. Please select accordingly ---> ")
        
        for book in self.book:
            print('Title:', book['Title'], ', Author:', book['Author'])
            
        print('-------------------------------------------------------------------------------------------------------')
        print('Enter Title For Edit Book --->')
        title = input()
        print('Enter Author For Edit Book --->')
        author = input()
        for book in self.book:
            if book['Title'] == title and book['Author'] == author:
                print('Enter New Title --> ')
                newTitle = input()
                print('Enter New Author --> ')
                newAuthor = input()
                book['Title'] = newTitle
                book['Author'] = newAuthor
        
        print('-----------------------------------------Book Edited Successfully!----------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        self.lms()  
                
    def show(self):
        print('-------------------------------------------------------------------------------------------------------')
        if not self.book:  
            print('No Book Yet!')
        else:
            for book in self.book:
                print('Title:', book['Title'], ', Author:', book['Author'])
    
        print('-------------------------------------------------------------------------------------------------------')
        self.lms()
    
    def Return(self , name , contact , email):
        print('-------------------------------------------------------------------------------------------------------')
        for reciver in self.bookReciver:
            if(reciver['Name'] == name and reciver['Contact'] == contact and reciver['Email'] == email):
                print('---Enter Title of the Book ---> ')
                title = input()
                print('---Enter Author of the Book ---> ')
                author = input()
                found = False
                for reciver in self.bookReciver:
                    if reciver['Book Title'] == title and reciver['Author'] == author:
                        self.bookReciver.remove(reciver)
                        self.book.append({"Title": title, "Author": author})
                        print('---Book Returned Successfully!---')
                        found = True
                        break
                if not found:
                    print('---Wrong Title or Author name for book!---')
                break
            else:
                print('---User Not Found!---')
        self.lms()
    
    def logout(self, admin_name):
        print('-------------------------------------------------------------------------------------------------------')
        print(f'------------------------------------See You Soon {admin_name}--------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print(f'------------------------------------Logout Time: {datetime.datetime.now().time()}--------------------------------------')
        main()
        
    def delete(self, title):
        print('-------------------------------------------------------------------------------------------------------')
        found = False
        for book in self.book[:]:
            if book['Title'] == title:
                self.book.remove(book) 
                print('---Book Deleted Successfully!---')
                found = True
                break
        if not found:
            print('---Book Not Found---')
        print('-------------------------------------------------------------------------------------------------------')
        self.lms()       
        
        
    def search(self , title):
        print('-------------------------------------------------------------------------------------------------------')
        found = False
        for book in self.book:
            if book['Title'] == title:
                print('Title:', book['Title'], ', Author:', book['Author'])
                found = True
        if not found:
            print('---Book Not Found---')
        print('-------------------------------------------------------------------------------------------------------')
        self.lms()
                               
        
    
    def lms(self):
        
        print('-------------------------------------------------------------------------------------------------------')
        print('Press 1 to Add Book ' + '\n' + 'Press 2 to Issue Book ' + '\n' + 
              'Press 3 to Edit Book ' + '\n' + 'Press 4 to Return Book ' + '\n' + 
              'Press 5 to Delete Book ' + '\n' + 'Press 6 to Search Book ' + '\n' + 
              'Press 7 to Show Book ' + '\n' + 'Press 8 to Logout ')
        print('-------------------------------------------------------------------------------------------------------')
    
        l = int(input())
        if l == 1:
            print('Enter Title of Book---> ')
            title = input()
            print('Enter Author of Book---> ')
            author = input()
            self.add(title, author)
            
        elif l == 2:
            print('Enter Your Name ---> ')
            name = input()
            print('Enter Your Phone Number ---> ')
            contact = input()
            print('Enter Your Email ---> ')
            email = input()
            self.issue(name , contact , email)
            
        elif l == 3:
            self.edit()
            
        elif l == 4:
            print('Enter Your Name ---> ')
            name = input()
            print('Enter Your Phone Number ---> ')
            contact = input()
            print('Enter Your Email ---> ')
            email = input()
            self.Return(name , contact , email)
        
        elif l == 5:
            print('Enter Title of Book For Delete---> ')
            title = input()
            self.delete(title)
            
        elif l == 6:
            print('Enter Title of Book For Search---> ')
            title = input()
            self.search(title)
            
        elif l == 7:
            self.show()
            
        elif l == 8:
            print('-------------------------------------------------------------------------------------------------------')
            print('Logging Out...')
            self.logout(Admin.AdminName)
    

class Admin:
    AdminId = 15437
    AdminPassword = 1114
    AdminName = 'Muhammad Siddiqui'
    time = datetime.datetime.now()
    
    def __init__(self , id , password ):
        self.id = id
        self.password = password 
        
    
    def changeNP(self , newName , newPassword):
        print('-------------------------------------------------------------------------------------------------------')
        Admin.AdminName = newName 
        Admin.AdminPassword = newPassword
        print('----------------------------------Password Updated Successfully!----------------------------------------')
        self.Dashboard()
        
        
        
        
    def Dashboard(self):
        print('-------------------------------------------------------------------------------------------------------')
        print(f'---------------------------------Welcome {Admin.AdminName}---------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print(f'-----------------------------------Time:{Admin.time.time()}------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print('Press 1 to Access Library Management System ' + '\n' + 
              'Press 2 to Access Your Profile ')
        adminPanel = int(input())
        if (adminPanel == 1):
            print('-------------------------------------------------------------------------------------------------------')
            print(f'-----------------------------------Welcome {Admin.AdminName} to Library MS-----------------------------')
            print('-------------------------------------------------------------------------------------------------------')
            obj = LMS()
            obj.lms()
        elif (adminPanel == 2):
            print('-------------------------------------------------------------------------------------------------------')
            print(f'-----------------------------------Welcome {Admin.AdminName} to Profile--------------------------------')
            print('-------------------------------------------------------------------------------------------------------')
            print('Press 1 to Change Personal Details ' + '\n' + 'Press 2 to View Personal Details ')
            a = int(input())
            if a == 1:
                print('Enter New Name--->')
                newName = input()
                print('Enter New Password--->')
                newPasword = int(input())
                self.changeNP(newName , newPasword)
                

def main():
    print('-------------------------------------------------------------------------------------------------------')
    print('---------------------------------Welcome To Library Management System----------------------------------')
    print('-------------------------------------------------------------------------------------------------------')
    print('---------Enter Your Id-----> ')
    id = int(input())
    print('---------Enter Your Password----->')
    password = int(input())
    a = Admin(id , password)
    if(Admin.AdminId == id and Admin.AdminPassword == password):
        print(Admin.time.time())
        a.Dashboard()
    else:
        print('Invalid ID or Password')
    
main()
