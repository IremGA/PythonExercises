'''
Created on Jul 20, 2017

Command Pattern has been used while implementing the scenario in Python. 
Client: Customer
Parent Command: Hobby 
Child Commands: BOOK,MUSIC,MOVIE and GAME
Director: HobbyMarket_Employee
Receiver: HobbyMarket 

@author: iaktas
'''

#define global variables
BOOK="book"
MUSIC="music"
MOVIE="movie"
GAME="game"

#Order
class Hobby(object):
    def __init__(self, title, release_date,hobby_type):
        self.title=title
        self.release_date=release_date
        self.hobby_type=hobby_type
        
#Child Orders
class Music(Hobby):
    def __init__(self, artist, album,title, release_date,hobby_type):
        Hobby.__init__(self,title, release_date,hobby_type)
        self.artist=artist
        self.album=album

class Movie(Hobby):
    def __init__(self, director, producer, title, release_date,hobby_type ):
        Hobby.__init__(self,title, release_date,hobby_type)
        self.director=director
        self.producer=producer
        
class Book(Hobby):
    def __init__(self, title, release_date, writer, publisher,hobby_type ):
        Hobby.__init__(self, title, release_date,hobby_type)       
        self.writer=writer
        self.publisher=publisher

class Game(Hobby):
    def __init__(self, title, release_date, mode, game_developer,hobby_type):
        Hobby.__init__(self, title, release_date,hobby_type)
        self.mode=mode
        self.game_developer=game_developer
#Receiver
class HobbyMarket(object):
    def __init__(self,name,hobbies):
        self.name=name
        self.hobbies=hobbies
    def searchHobbyByTitle(self, hobby):
        '''filter operation restuns a list'''
        results =  filter(lambda x: x.title == hobby.title, self.hobbies)
        return results
    def searchHobbyByReleaseDate(self, hobby):
        '''filter operation restuns a list'''
        results= filter(lambda x: x.release_date == hobby.release_date, self.hobbies)
        return results
    
#Director                   
class HobbyMarket_Employee(object): 
        def __init__(self, employee_number, hobbyMarket):
            self.employee_number =employee_number
            self.hobbyMarket = hobbyMarket
        def printResuts(self, results):
            if len(results) == 0:
                print "There is no record to print!!"
            else:
                for result in results:
                    print "Title : " + result.title
                    print "Release Date : " + result.release_date
                    if result.hobby_type == BOOK : 
                        print "Writer : " + result.writer
                        print "Publisher : " + result.publisher
                    elif result.hobby_type == MUSIC:
                        print "Artist : " + result.artist
                        print "Album Name : " + result.album
                    elif result.hobby_type == GAME:
                        print "Mode : " + result.mode
                        print "Game Developer Company : " + result.game_developer
                    elif result.hobby_type == MOVIE:
                        print "Director : " + result.director
                        print "Producer : " + result.producer
        def do_hobbySearch(self,hobby):
            print "Hello my number is "+self.employee_number+". Welcome to "+self.hobbyMarket.name+" Hobby Shop! I'm searching .."
            if hobby.title == "" or hobby.title is None:
                results = self.hobbyMarket.searchHobbyByReleaseDate(hobby)
                if len(results)> 0:
                    print "There is "+str(len(results))+ " record/s found for "+hobby.release_date
                    print "Let me show you the results:  "
                    self.printResuts(results)
                else:
                    print "Sorry No result found for "+hobby.title
                
            elif hobby.release_date == "" or hobby.release_date is None:
                results =self.hobbyMarket.searchHobbyByTitle(hobby)
                if len(results)> 0:
                    print "There is "+str(len(results))+ " record/s found for "+hobby.title
                    print "Let me show you the results:  "
                    self.printResuts(results)
                else:
                    print "Sorry No result found for "+hobby.title

#Client
class Customer(object):
    def __init__(self, name): 
        self.name = name;
    def search_hobby(self, hobby, hobbyMarket_Employee):
        print"Hello I want you to  search "+hobby.title + hobby.release_date
        hobbyMarket_Employee.do_hobbySearch(hobby)

def main():
    
    customerX = Customer("XX")
    customerY = Customer("YY")
    
    guardians_of_the_Galaxy = Movie("James Gunn", "Marvel", "Guardians Of the Galaxy", "2014",MOVIE)
    guardians_of_the_Galaxy2 = Movie("James Gunn", "Marvel", "Guardians Of the Galaxy 2", "2017",MOVIE)
    john_Wick = Movie("Chad Stahelski, David Leitch", "Basil Iwanyk, David Leitch, Eva Longoria,Michael Witherill", "John Wick", "2014",MOVIE)
    john_Wick2 = Movie("Chad Stahelski", "Basil Iwanyk, David Leitch, Eva Longoria", "John Wick 2", "2017",MOVIE)
    logan = Movie("James Mangold","Hutch Parker, Simon Kinberg, Lauren Shuler Donner ","Logan","2017", MOVIE)
   
    man_of_war =Music("Radiohead", "Man of War", "OK COMPUTER OKNOTOK", "2017",MUSIC)
    highway = Music("Chris Cornell", "Songbook", "I am the hiqhway", "2011", MUSIC)
    canTStop = Music("Red Hot Chili Peppers", "By the way", "Can't Stop", "2002", MUSIC)
    psycho = Music("Muse", "Drones", "Psycho", "2015", MUSIC)
    nutshell = Music("Alice In Chains","NutShell", "Jar of Flies", "1994", MUSIC)
    
    nineteeneightyfour_Novel = Book("1984", "George Orwell", "Harvil Secker","1948",BOOK)
    new_brave_world =  Book("New Brave World", "Aldoux Huxley", "Perennial, Reprint", "1932",BOOK)
    clock_work_orange = Book("Clockwork Orange","Anthony Burgess", "X", "1962",BOOK)
    kill_mockingbird = Book("To Kill a Mockingbird", "Harper Lee", "Sel", "1960", BOOK)
    
    army_of_two = Game("Army of Two ", "2013", "co-op", "Electronic Arts",GAME)
    resistance = Game("Resistance ", "2006", "co-op", "Insomaniac Games",GAME)
    fear_3 = Game("F.E.A.R. 3", "2011", "co-op", "Wargaming Chicago-Baltimore",GAME)
    borderlands = Game("Borderlands", "2009", "co-op", "Gearbox ",GAME)
    
    hobbies_for_HobbyMarket1 = [guardians_of_the_Galaxy,logan,man_of_war,psycho, nutshell,nineteeneightyfour_Novel,new_brave_world,army_of_two,resistance,fear_3 ]
    hobbies_for_HobbyMarket2 = [guardians_of_the_Galaxy2,john_Wick, john_Wick2,logan,highway, canTStop, clock_work_orange,kill_mockingbird, borderlands]
    
    hobbyMarket1 = HobbyMarket("D&R", hobbies_for_HobbyMarket1)
    hobbyMarket2 = HobbyMarket("Remzi", hobbies_for_HobbyMarket2)
    
    hobbyMarket_Employee1 = HobbyMarket_Employee("111",hobbyMarket1 ) 
    hobbyMarket_Employee2 = HobbyMarket_Employee("000",hobbyMarket2 ) 
    
    hobby_will_searched_by_customer_1 = Hobby("New Brave World", "", BOOK)
    hobby_will_searched_by_customer_2= Hobby("","2013",GAME)
    
    customerX.search_hobby(hobby_will_searched_by_customer_1, hobbyMarket_Employee1)
    print ""
    customerX.search_hobby(hobby_will_searched_by_customer_1,hobbyMarket_Employee2)
    print ""
    customerY.search_hobby(hobby_will_searched_by_customer_2, hobbyMarket_Employee1)
    print ""
    customerY.search_hobby(hobby_will_searched_by_customer_2, hobbyMarket_Employee2)
    
    
if  __name__ =='__main__':
    main()
