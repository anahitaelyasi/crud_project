from crud import *
from db import SessionLocal


def is_zero(var) :
    if var == "0" or var == 0 :
        return 0

def user(db) :
    while True :
        print("\nTable User selected.") 
        user_choice = input("\nChoose an action in CRUD (C,R,U,D) / enter 0 to back to main menu : ")

        match user_choice :
            case "C" :
                while True : 
                    print("\nEnter the required attributes to create new user!")
                    name, email, phone_number, password, role = '','','','',''
                    is_empty = False
                    for i in range(1,6) :
                        match i :
                            case 1 :
                                name = input("\nname : ") 
                                if name == "0" or name == '':
                                    is_empty = True 
                                    break 
                            case 2 :
                                email = input("\nemail : ")
                                if email == "0" or email == '':
                                    is_empty = True
                                    break
                            case 3 : 
                                phone_number = input("\nphone_number : ")
                                if phone_number == "0" or phone_number == '':
                                    is_empty = True
                                    break
                            case 4 :
                                password = input("\npassword : ")
                                if password == "0" or password == '':
                                    is_empty = True
                                    break
                            case 5 :
                                role = input("\nrole : ")
                                if role == "0" or role == '':
                                    is_empty = True 
                                    break
                    
                    if is_empty :
                        break 
                    new_user = create_user(db=db, name=name, email=email, phone_number=phone_number, password=password, role=role)
                    if new_user == None : 
                        continue     
                    print(f"\nNew user : \nname = {new_user.name} \nemail = {new_user.email} \nphone_number = {new_user.phone_number} \npassword = {new_user.password} \nrole = {new_user.role}") 
                    break 

            case "R" :
                while True : 
                    print("\nEnter the required attributes to get user by id!")
                    user_id = input("\nuser_id (enter 0 to step back): ") 
                    if user_id == "0" :
                        break 
                    else : 
                        get_user = retrieving_user(db=db, user_id=user_id) 
                        if get_user == None :
                            continue 
                        print(f"\nThis is the user you asked for : \nname = {get_user.name} \nemail = {get_user.email} \nphone_number = {get_user.phone_number} \npassword = {get_user.password} \nrole = {get_user.role}")
                        break 

            case "U" :
                user_id = int(input("\nEnter user_id : "))
                print("\nEnter one attribute to update in user!")
                attribute = input("\nSelect an attribute (name email phone_number password role) : ") 
                new_value = input(f"\nEnter a new value for user.{attribute} : ") 
                user_updated = update_user(db=db, user_id=user_id, attribute=attribute, new_value=new_value) 
                print(f"\nUser info updated : name = {user_updated.name}\nemail = {user_updated.email} \nphone_number = {user_updated.phone_number} \npassword = {user_updated.password} \nrole = {user_updated.role}") 

            case "D" :
                user_id = int(input("\nEnter user_id you want to delete : ")) 
                deleted_user = delete_user(db=db, user_id=user_id) 
                if deleted_user : 
                    print(f"\nUser deleted.") 
            
            case "0" :
                main_menu() 
                break 


def hotel(db) :
    while True :
        print("\nTable Hotel selected.") 
        user_choice = input("\nChoose an action in CRUD (C,R,U,D) / enter 0 to back to main menu : ")

        match user_choice :
            case "C" : 
                while True : 
                    print("\nEnter the required attributes to create new hotel!")
                    name, location, rating = '','',''
                    is_empty = False 
                    for i in range(1,4) :
                        match i :
                            case 1 :
                                name = input("\nname : ") 
                                if name == "0" or name == '':
                                    is_empty = True 
                                    break 
                            case 2 :
                                location = input("\nemail : ")
                                if location == "0" or location == '':
                                    is_empty = True
                                    break
                            case 3 : 
                                rating = input("\nphone_number : ")
                                if rating == "0" or rating == '':
                                    is_empty = True
                                    break
                    
                    if is_empty :
                        break 
                    new_hotel = create_hotel(db=db, location=location, name=name, rating=rating)
                    if new_hotel == None : 
                        continue     
                    print(f"\nNew hotel : \nname = {new_hotel.name} \nlocation = {new_hotel.location} \nrating = {new_hotel.rating}") 
                    break 

            case "R" :

                while True : 
                    print("\nEnter the required attributes to get hotel by id!")
                    hotel_id = input("\nhotel_id (enter 0 to step back): ") 
                    if hotel_id == "0" :
                        break 
                    else : 
                        get_hotel = retrieving_hotel(db=db, hotel_id=hotel_id) 
                        if get_hotel == None :
                            continue 
                        print(f"\nThis is the hotel you asked for : \nname = {get_hotel.name} \nlocation = {get_hotel.location} \nrating = {get_hotel.rating}")
                        break 

            case "U" :
                hotel_id = input("\nEnter hotel_id : ")
                print("\nEnter one attribute to update in hotel!")
                attribute = input("\nSelect an attribute (name location rating) : ")
                new_value = input(f"\nEnter a new value for hotel.{attribute} : ") 
                hotel_updated = update_hotel(db=db, hotel_id=hotel_id, attribute=attribute, new_value=new_value) 
                print(f"Hotel info updated : \nname = {hotel_updated.name} \nlocation = {hotel_updated.location} \nrating = {hotel_updated.rating}") 



            case "D" :
                hotel_id = input("\nEnter hotel_id you want to delete : ") 
                deleted_hotel = delete_hotel(db=db, hotel_id=hotel_id) 
                if deleted_hotel :
                    print(f"Hotel deleted.")
            
            case "0" :
                main_menu() 
                break 
def room(db) :
    while True :
        print("\nTable Room selected.") 
        user_choice = input("\nChoose an action in CRUD (C,R,U,D) / enter 0 to back to main menu : ")

        match user_choice :
            case "C" :
                while True : 
                    print("\nEnter the required attributes to create new room!")
                    room_type, room_number, status, max_guests, price_per_night = '','','','',''
                    is_empty = False 
                    for i in range(1,6) :
                        match i :
                            case 1 :
                                room_type = input("\nroom_type : ") 
                                if room_type == "0" or room_type == '':
                                    is_empty = True 
                                    break 
                            case 2 :
                                room_number = input("\nroom_number : ")
                                if room_number == "0" or room_number == '':
                                    is_empty = True
                                    break
                            case 3 : 
                                status = input("\nstatus : ")
                                if status == "0" or status == '':
                                    is_empty = True
                                    break
                            case 4 :
                                max_guests = input("\nmax_guests : ")
                                if max_guests == "0" or max_guests == '':
                                    is_empty = True
                                    break
                            case 5 : 
                                price_per_night = input("\nprice_per_night : ")
                                if price_per_night == "0" or price_per_night == '':
                                    is_empty = True
                                    break
                    
                    if is_empty :
                        break 
                    new_room = create_room(db=db, room_type=room_type, room_number=room_number, status=status, max_guests=max_guests, price_per_night=price_per_night) 

                    if new_room == None : 
                        continue     
                    print(f"\nNew room : \nroom_type = {new_room.room_type} \nroom_number = {new_room.room_number} \nstatus = {new_room.status}" + 
                          f"\nmax_guests = {new_room.max_guests} \nprice_per_night = {new_room.price_per_night}") 
                    break 

            case "R" :
                 
                while True : 
                    print("\nEnter the required attributes to get room by id!")
                    room_id = input("\nroom_id (enter 0 to step back): ") 
                    if room_id == "0" :
                        break 
                    else : 
                        get_room = retrieving_room(db=db, room_id=room_id) 
                        if get_room == None :
                            continue 
                        print(f"\nThis is the room you asked for : \nroom_type = {new_room.room_type} \nroom_number = {new_room.room_number} \nstatus = {new_room.status}" + 
                          f"\nmax_guests = {new_room.max_guests} \nprice_per_night = {new_room.price_per_night}")
                        break

            case "U" :
                room_id = input("\nEnter room_id : ")
                print("\nEnter one attribute to update in room!") 
                attribute = input("\nChoose an attribute (room_type room_number status max_guests price_per_night) : ")
                new_value = input(f"\nEnter a new value for room.{attribute} : ") 
                room_updated = update_room(db=db, room_id=room_id, attribute=attribute, new_value=new_value) 
                print(f"\nRoom info updated : \nroom_type = {room_updated.room_type} \nroom_number = {room_updated.room_number} \nstatus = {room_updated.status}" + 
                          f"\nmax_guests = {room_updated.max_guests} \nprice_per_night = {room_updated.price_per_night}") 


            case "D" :
                room_id = input("\nEnter room_id you want to delete!") 
                deleted_room = delete_room(db=db, room_id=room_id) 
                if delete_room : 
                    print(f"\nRoom deleted.")
            
            case "0" :
                main_menu() 
                break 

def reservation(db) :
    while True :
        print("\nTable Reservation selected.") 
        user_choice = input("\nChoose an action in CRUD (C,R,U,D) / enter 0 to back to main menu : ")

        match user_choice :
            case "C" :                
                while True : 
                    print("\nEnter the required attributes to create new discount!")
                    number_of_guests, checkIn_date, checkOut_date  = '','','',''
                    is_empty = False 
                    for i in range(1,6) :
                        match i :
                            case 1 :
                                number_of_guests = input("\nnumber_of_guests : ") 
                                if number_of_guests == "0" or number_of_guests == '':
                                    is_empty = True 
                                    break 
                            case 2 :
                                checkIn_date = input("\ncheckIn_date : ")
                                if checkIn_date == "0" or checkIn_date == '':
                                    is_empty = True
                                    break
                            case 3 : 
                                checkOut_date = input("\ncheckOut_date : ")
                                if checkOut_date == "0" or checkOut_date == '':
                                    is_empty = True
                                    break
                    
                    if is_empty :
                        break 
                    new_reservation = create_reservation(db=db, number_of_guests=number_of_guests, checkIn_date=checkIn_date, checkOut_date=checkOut_date) 
                    if new_reservation == None : 
                        continue     
                    print(f"\nNew reservation : \nnumber_of_guests = {new_reservation.number_of_guests} \ncheckIn_date = {new_reservation.checkIn_date} \ncheckOut_date = {new_reservation.checkOut_date}") 
                    break

            case "R" :
                
                while True : 
                    print("\nEnter the required attributes to get reservation by id!")
                    reservation_id = input("\nreservation_id (enter 0 to step back): ") 
                    if reservation_id == "0" :
                        break 
                    else : 
                        get_reservation = retrieving_reservation(db=db, reservation_id=reservation_id)  
                        if get_reservation == None :
                            continue 
                        print(f"\nThis is the reservation you asked for : \nnumber_of_guests = {get_reservation.number_of_guests} \ncheckIn_date = {get_reservation.checkIn_date} \ncheckOut_date = {get_reservation.checkOut_date}")
                        break

            case "U" :
                discount_id = input("\nEnter discount_id : ") 
                print("\nEnter one attribute to update in discount!")
                attribute = input("\nChoose an attribute (name location rating) : ")
                new_value = input(f"\nEnter a new value for discount.{attribute} : ") 
                discount_updated = update_reservation(db=db, discount_id=discount_id, attribute=attribute, new_value=new_value) 
                print(f"\nDiscount info updated : \nnumber_of_guests = {discount_updated.number_of_guests} \ncheckIn_date = {discount_updated.checkIn_date} \ncheckOut_date = {discount_updated.checkOut_date}") 

            case "D" :
                discount_id = input("\nEnter discount_id you want to delete!") 
                deleted_discount = delete_reservation(db=db, discount_id=discount_id) 
                if delete_discount : 
                    print(f"\nDiscount deleted.")
            
            case "0" :
                main_menu() 
                break 


def discount(db) :
    while True :
        print("\nDiscount Discount selected.") 
        user_choice = input("\nChoose an action in CRUD (C,R,U,D) / enter 0 to back to main menu : ")

        match user_choice :
            case "C" :
                while True : 
                    print("\nEnter the required attributes to create new discount!")
                    status, discount_percentage, code  = '','',''
                    is_empty = False 
                    for i in range(1,6) : 
                        match i :
                            case 1 :
                                status = input("\nstatus : ") 
                                if status == "0" or status == '':
                                    is_empty = True 
                                    break  
                            case 2 :
                                discount_percentage = input("\ndiscount_percentage : ")
                                if discount_percentage == "0" or discount_percentage == '':
                                    is_empty = True
                                    break
                            case 3 : 
                                code = input("\ncode : ")
                                if code == "0" or code == '':
                                    is_empty = True
                                    break
                    
                    if is_empty :
                        break 
                    new_discount = create_discount(db=db, status=status, discount_percentage=discount_percentage, code=code) 
 
                    if new_discount == None : 
                        continue     
                    print(f"\nNew reservation : \nstatus = {new_discount.status} \ndiscount_percentage = {new_discount.discount_percentage} \ncode = {new_discount.code}") 
                    break 

            case "R" :

                while True : 
                    print("\nEnter the required attributes to get discount by id!")
                    discount_id = input("\ndiscount_id (enter 0 to step back): ") 
                    if discount_id == "0" :
                        break 
                    else : 
                        get_discount = retrieving_discount(db=db, discount_id=discount_id)  
                        if get_discount == None :
                            continue 
                        print(f"\nThis is the discount you asked for : \nstatus = {get_discount.status} \ndiscount_percentage = {get_discount.discount_percentage} \ncode = {get_discount.code}")
                        break

            case "U" :
                hotel_id = input("\nEnter hotel_id : ")
                print("\nEnter one attribute to update in hotel!")
                attribute = input("\nChoose an attribute (name location rating) : ")
                new_value = input(f"\nEnter a new value for hotel.{attribute} : ") 
                hotel_updated = update_hotel(db=db, hotel_id=hotel_id, attribute=attribute, new_value=new_value) 
                print(f"Hotel info updated : \nstatus = {hotel_updated.status} \ndiscount_percentage = {hotel_updated.discount_percentage} \ncode = {hotel_updated.code}") 

            case "D" :
                hotel_id = input("\nEnter hotel_id you want to delete!") 
                deleted_hotel = delete_hotel(db=db, hotel_id=hotel_id)
                if delete_hotel :  
                    print(f"Hotel deleted.")
            
            case "0" :
                main_menu() 
                break 

def payment(db) :
    while True :
        print("\nTable Payment selected.") 
        user_choice = input("\nChoose an action in CRUD (C,R,U,D) / enter 0 to back to main menu : ")

        match user_choice :
            case "C" :                
                while True : 
                    print("\nEnter the required attributes to create new payment!")
                    payment_methods, payment_status, payment_date,  = '','','',''
                    is_empty = False 
                    for i in range(1,6) :
                        match i :
                            case 1 :
                                payment_methods = input("\npayment_methods : ") 
                                if payment_methods == "0" or payment_methods == '':
                                    is_empty = True 
                                    break  
                            case 2 :
                                payment_status = input("\npayment_status : ")
                                if payment_status == "0" or payment_status == '':
                                    is_empty = True
                                    break
                            case 3 : 
                                payment_date = input("\npayment_date : ")
                                if payment_date == "0" or payment_date == '':
                                    is_empty = True
                                    break
                            case 4 :
                                payment_amount = input("\npayment_amount : ")
                                if payment_amount == "0" or payment_amount == '':
                                    is_empty = True
                                    break
                    
                    if is_empty :
                        break 
                    new_payment = create_payment(db=db, payment_methods=payment_methods, payment_status=payment_status, payment_date=payment_date, payment_amount=payment_amount) 
 
                    if new_payment == None : 
                        continue     
                    print(f"\nNew reservation : \nstatus = {new_payment.payment_methods} \npayment_status = {new_payment.payment_status} \npayment_date = {new_payment.payment_date} \npayment_amount = {new_payment.payment_amount}") 
                    break 

            case "R" :

                while True : 
                    print("\nEnter the required attributes to get payment by id!")
                    payment_id = input("\npayment_id (enter 0 to step back): ") 
                    if payment_id == "0" :
                        break 
                    else : 
                        get_payment = retrieving_payment(db=db, payment_id=payment_id)  
                        if get_payment == None :
                            continue 
                        print(f"\nThis is the payment you asked for : \nstatus = {get_payment.payment_methods} \npayment_status = {get_payment.payment_status} \npayment_date = {get_payment.payment_date} \npayment_amount = {get_payment.payment_amount}")
                        break 

            case "U" :
                hotel_id = input("\nEnter hotel_id : ")
                print("\nEnter one attribute to update in hotel!")
                attribute = input("\nChoose an attribute (name location rating) : ")
                new_value = input(f"\nEnter a new value for hotel.{attribute} : ") 
                hotel_updated = update_hotel(db=db, hotel_id=hotel_id, attribute=attribute, new_value=new_value) 
                print(f"Hotel info updated : \nstatus = {hotel_updated.payment_methods} \npayment_status = {hotel_updated.payment_status} \npayment_date = {hotel_updated.payment_date} \npayment_amount = {hotel_updated.payment_amount}") 

            case "D" :
                hotel_id = input("\nEnter hotel_id you want to delete!") 
                deleted_hotel = delete_hotel(db=db, hotel_id=hotel_id) 
                print(f"Hotel deleted : {deleted_hotel}")
            
            case "0" :
                main_menu() 
                break  

def review(db) :
    while True :
        print("\nTable Review selected.") 
        user_choice = input("\nChoose an action in CRUD (C,R,U,D) / enter 0 to back to main menu : ")

        match user_choice :
            case "C" :
                while True : 
                    print("\nEnter the required attributes to create new review!")
                    user_id, hotel_id, comment, rating, review_date,  = '', '', '', '', ''
                    is_empty = False 
                    for i in range(1,6) :
                        match i :
                            case 1 :
                                user_id = int(input("\nuser_id : ")) 
                                if user_id == 0 or user_id == '':
                                    is_empty = True 
                                    break 
                            case 2 :
                                hotel_id = int(input("\nhotel_id : ")) 
                                if hotel_id == 0 or hotel_id == '':
                                    is_empty = True 
                                    break 
                            case 3 :
                                comment = input("\ncomment : ") 
                                if comment == "0" or comment == '':
                                    is_empty = True 
                                    break  
                            case 4 :
                                rating = int(input("\nrating : "))
                                if rating == 0 or rating == '':
                                    is_empty = True
                                    break
                            case 5 : 
                                review_date = input("\nreview_date : ")
                                if review_date == "0" or review_date == '':
                                    is_empty = True
                                    break 
                    
                    if is_empty :
                        break 
                    new_review = create_review(db=db, user_id=user_id, hotel_id=hotel_id, comment=comment, rating=rating, review_date=review_date) 
 
                    if new_review == None : 
                        continue     
                    print(f"\nNew reservation : \ncomment = {new_review.comment} \nrating = {new_review.rating} \nreview_date = {new_review.review_date}") 
                    break 

            case "R" :

                while True : 
                    print("\nEnter the required attributes to get review by id!")
                    review_id = input("\nreview_id (enter 0 to step back): ") 
                    if review_id == "0" :
                        break 
                    else : 
                        get_review = retrieving_review(db=db, review_id=review_id)  
                        if get_review == None :
                            continue 
                        print(f"\nThis is the review you asked for : \ncomment = {get_review.comment} \nrating = {get_review.rating} \nreview_date = {get_review.review_date}")
                        break 

            case "U" :
                review_id = input("\nEnter review_id : ")
                print("\nEnter one attribute to update in review!")
                attribute = input("\nChoose an attribute (comment rating review_date) : ")
                new_value = input(f"\nEnter a new value for review.{attribute} : ") 
                review_updated = update_review(db=db, review_id=review_id, attribute=attribute, new_value=new_value) 
                print(f"Review info updated : \ncomment = {review_updated.comment} \nrating = {review_updated.rating} \nreview_date = {review_updated.review_date}") 

            case "D" :
                review_id = input("\nEnter review_id you want to delete!") 
                deleted_review = delete_review(db=db, review_id=review_id) 
                if delete_review : 
                    print(f"Hotel deleted : {deleted_review}")
            
            case "0" :
                main_menu() 
                break  


def main_menu() :
    db = SessionLocal()

    while True :
        print("\nMain menu")
        print("\nTables are : ")
        print("1.User\n2.Hotel\n3.Room\n4.Reservation\n5.Discount\n6.Payment\n7.Review")
        user_choice = int(input("\nChoose a table (1,2,3,4,5,6,7) / enter 0 to exit : ")) 

        match user_choice :
            case 1 :
                user(db)
                break 
            case 2 :
                hotel(db)
                break
            case 3 :
                room(db)
                break
            case 4 :
                reservation(db)
                break
            case 5 :
                discount(db)
                break
            case 6 :
                payment(db)
                break
            case 7 :
                review(db) 
                break
            case 0 :
                break  
  

main_menu()

print("Bye Bye!") 