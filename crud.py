#defines your CRUD functions
from models import *
from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import insert, delete

from db import SessionLocal


db = SessionLocal()


#------------------------------------------------------------------------------------------------------------
#---------------------------------------------user crud------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

def create_user(db: Session, name: str, email: str, phone_number: int, password: str, role: str) :
    user = User(name= name, email= email, phone_number= phone_number, password= password, role= role) 
    if user : 
        allowed_roles = {'guest', 'crews', 'manager'}
        if role not in allowed_roles :
            print(f"Invalid role. Must be one of {allowed_roles}")
            return None 
        db.add(user)
        db.commit()
        db.refresh(user) 
        return user 

def retrieving_user(db: Session, user_id: int) :
    get_user = db.query(User).filter(User.user_id == user_id).first() 
    if get_user :
        return get_user 
    else :
        print("user_id doesn't exist!\nPlease enter a new user_id.") 
        return None 

def update_user(db: Session, user_id: int, attribute, new_value) :
    dict = ["name", "email", "phone_number", "password", "role"] 
    user = db.query(User).filter(User.user_id == user_id).first()
        
    if user : 
        if attribute in dict : 
            setattr(user, attribute, new_value)  
            db.commit()
            db.refresh(user)
            return user
        else :
            print("Attribute doesn't exist!\nPlease enter a new attribute.")
            return None 
    else :
        print("user_id doesn't exist!\nPlease enter a new user_id.")
        return None 

def delete_user(db: Session, user_id: int) :
    user = db.query(User).filter(User.user_id == user_id).first() 
    if user :
        db.delete(user)
        db.commit() 
        return True 
    print("Invalid user_id.\nPlease enter a new one!")
    return None

#------------------------------------------------------------------------------------------------------------
#---------------------------------------------hotel crud-----------------------------------------------------
#------------------------------------------------------------------------------------------------------------

def create_hotel(db: Session, location: str, name: str, rating: int) :
    hotel = Hotel(location= location, name= name, rating= rating) 
    if hotel :
        db.add(hotel)
        db.commit()
        db.refresh(hotel)
        return hotel 
 
def retrieving_hotel(db: Session, hotel_id: int) :
    get_hotel = db.query(Hotel).filter(Hotel.hotel_id == hotel_id).all()
    if get_hotel :
        return get_hotel 
    else :
        print("user_id doesn't exist!\nPlease enter a new user_id.") 
        return None  

def update_hotel(db: Session, hotel_id: int, attribute, new_value) :
    hotel = db.query(Hotel).filter(Hotel.hotel_id == hotel_id).first()
    dict = ["name", "location", "rating"]
    if hotel : 
        if attribute in dict :
            setattr(hotel, attribute, new_value) 
            db.commit()
            db.refresh(hotel) 
            return hotel 
        else :
            print("Attribute doesn't exist!\nPlease enter a new attribute.")
            return None
    else :
        print("hotel_id doesn't exist!\nPlease enter a new hotel_id.")
        return None


def delete_hotel(db: Session, hotel_id: int) :
    hotel = db.query(Hotel).filter(Hotel.hotel_id == hotel_id).first() 
    if hotel :
        db.delete(hotel) 
        db.commit()
        return True 
    print("Invalid hotel_id.\nPlease enter a new one!")
    return None

#------------------------------------------------------------------------------------------------------------
#---------------------------------------------room crud------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

def create_room(db: Session, room_type: str, room_number: int, status: str, max_guests: int, price_per_night: float) :
    room = Room(room_type= room_type, room_number= room_number, status= status, max_guests= max_guests, price_per_night= price_per_night) 
    if room :
        allowed_room_types = ['single','double','suite']
        allowed_room_status = ['available','reserved','out of service']
        if room_type not in allowed_room_types :
            print(f"\nInvalid room type. Must be one of {allowed_room_types} ")
            return None
        if status not in allowed_room_status :
            print(f"Invalid room status. Must be one of {allowed_room_status}") 
            return None
        db.add(room)
        db.commit()
        db.refresh(room)
        return room

def retrieving_room(db: Session, room_id: int) :
    get_room =  db.query(Room) .filter(Room.room_id == room_id).all() 
    if get_room :
        return get_room 
    else :
        print("room_id doesn't exist!\nPlease enter a new room_id.") 
        return None 

def update_room(db: Session, room_id: int, attribute, new_value) :
    room = db.query(Room).filter(Room.room_id == room_id).first()
    dict = ["room_type", "room_number", "status", "max_guests", "price_per_night"]
    if room : 
        if attribute in dict :
            setattr(room, attribute, new_value)  
            db.commit()
            db.refresh(room)
            return room
        else :
            print("Attribute doesn't exist!\nPlease enter a new attribute.")
            return None
    else :
        print("room_id doesn't exist!\nPlease enter a new room_id.")
        return None 


def delete_room(db: Session, room_id: int) :
    room = db.query(Room).filter(Room.room_id == room_id).first() 
    if room :
        db.delete(room)
        db.commit()
        return True 
    print("Invalid room_id.\nPlease enter a new one!")
    return None

#------------------------------------------------------------------------------------------------------------
#---------------------------------------------Reservation crud-----------------------------------------------
#------------------------------------------------------------------------------------------------------------

def create_reservation(db: Session, number_of_guests: int, checkIn_date: date, checkOut_date: date) :
    reservation = Reservation(number_of_guests= number_of_guests, checkIn_date= checkIn_date, checkOut_date= checkOut_date) 
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation

def retrieving_reservation(db: Session, reservation_id: int) :
    get_reservation = db.query(Reservation).filter(Reservation.reservation_id == reservation_id).all() 
    if get_reservation :
        return get_reservation 
    else :
        print("reservation_id doesn't exist!\nPlease enter a new reservation_id.") 
        return None 

def update_reservation(db: Session, reservation_id: int, attribute, new_value) :
    reservation = db.query(Reservation).filter(Reservation.reservation_id == reservation_id).first()
    dict = ["number_of_guests", "checkIn_date", "checkOut_date"]
    if reservation : 
        if attribute in dict :
            setattr(reservation, attribute, new_value) 
            db.commit()
            db.refresh(reservation)
            return reservation
        else :
            print("Attribute doesn't exist!\nPlease enter a new attribute.")
            return None 
    else :
        print("reservation_id doesn't exist!\nPlease enter a new reservation_id.")
        return None


def delete_reservation(db: Session, reservation_id: int) :
    reservation = db.query(Reservation).filter(Reservation.reservation_id == reservation_id).first() 
    if reservation :
        db.delete(reservation)
        db.commit()
        return True
    print("Invalid reservation_id.\nPlease enter a new one!")
    return None

#------------------------------------------------------------------------------------------------------------
#---------------------------------------------Reserve_Room crud----------------------------------------------
#------------------------------------------------------------------------------------------------------------


def add_user(db: Session, reservation_id: int, room_id: int) :
    db.execute(
        insert(Reserve_Room).values(reservation_id=reservation_id, room_id=room_id)
    )
    db.commit()

def delete_data(db: Session, reservation_id: int, room_id: int) :
    db.execute(
        delete(Reserve_Room).where(
            (Reserve_Room.reservation_id == reservation_id) &
            (Reserve_Room.room_id == room_id)
        )
    )
    db.commit()


#------------------------------------------------------------------------------------------------------------
#---------------------------------------------Reserve_Hotel crud------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

def add_hotel_to_reservation(db: Session, reservation_id: int, hotel_id: int):
    db.execute(
        insert(Reserve_Hotel).values(reservation_id=reservation_id, hotel_id=hotel_id)
    )
    db.commit()


def remove_hotel_from_reservation(db: Session, reservation_id: int, hotel_id: int):
    db.execute(
        delete(Reserve_Hotel).where(
            (Reserve_Hotel.reservation_id == reservation_id) &
            (Reserve_Hotel.hotel_id == hotel_id)
        )
    )
    db.commit()



#------------------------------------------------------------------------------------------------------------
#---------------------------------------------Discount crud------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

def create_discount(db: Session, status: str, discount_percentage : float, code: str) :
    discount = Discount(status= status, discount_percentage= discount_percentage, code= code) 
    if discount : 
        allowed_status = ['active','expired']
        if not 0 <= discount_percentage <= 100 :
            print("\nDiscount percentage should be between 0% to 100%.")
            return None 
        if status not in allowed_status :
            print(f"\nInvalid discount status. Must be one of {allowed_status}.")
            return None
        db.add(discount)
        db.commit()
        db.refresh(discount)
        return discount

def retrieving_discount(db: Session, discount_id: int) :
    get_discount =  db.query(Discount).filter(Discount.discount_id == discount_id).all()
    if get_discount :
        return get_discount
    else :
        print("discount_id doesn't exist!\nPlease enter a new discount_id.") 
        return None  

def update_discount(db: Session, discount_id: int, attribute, new_value) :
    discount = db.query(Discount).filter(Discount.discount_id == discount_id).first()
    dict = ["status", "discount_percentage", "code"] 
    if discount : 
        if attribute in dict :
            setattr(discount, attribute, new_value)
            db.commit()
            db.refresh(discount) 
            return discount
        else :
            print("Attribute doesn't exist!\nPlease enter a new attribute.")
            return None
    else :
        print("discount_id doesn't exist!\nPlease enter a new discount_id.") 
        return None

def delete_discount(db: Session, discount_id: int) :
    discount = db.query(Discount).filter(Discount.discount_id == discount_id).first() 
    if discount :
        db.delete(discount)
        db.commit()
        return True
    print("Invalid discount_id.\nPlease enter a new one!")
    return None


#------------------------------------------------------------------------------------------------------------
#---------------------------------------------Payment crud---------------------------------------------------
#------------------------------------------------------------------------------------------------------------

def create_payment(db: Session, payment_methods : str, payment_status : str, payment_date : date, payment_amount: float) :
    payment = Payment(payment_methods= payment_methods, payment_status= payment_status, payment_date= payment_date, payment_amount= payment_amount) 
    if payment :
        allwed_payment_methods = ['cash','online']
        allwed_payment_status = ['Paid', 'Cancelled', 'Pending']
        if payment_methods not in allwed_payment_methods :
            print(f"Invalid payment method. Must be one of {allwed_payment_methods}")
            return None 
        if payment_status not in allwed_payment_status : 
            print(f"Invalid payment status. Must be one of {allwed_payment_status}") 
            return None
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment 

def retrieving_payment(db: Session, payment_id: int) :
    get_payment = db.query(Payment).filter(Payment.payment_id == payment_id).all() 
    if get_payment :
        return get_payment 
    else :
        print("payment_id doesn't exist!\nPlease enter a new payment_id.") 
        return None 

def update_payment(db: Session, payment_id: int, attribute, new_value) :
    payment = db.query(Payment).filter(Payment.payment_id == payment_id).first()
    dict = ["payment_methods", "payment_status", "payment_date", "payment_amount", ""]
    if payment : 
        if attribute in dict :
            setattr(payment, attribute, new_value)
            db.commit()
            db.refresh(payment) 
            return payment 
        else :
            print("Attribute doesn't exist!\nPlease enter a new attribute.")
            return None
    else :
        print("payment_id doesn't exist!\nPlease enter a new payment_id.") 
        return None
        

def delete_payment(db: Session, payment_id: int) :
    payment = db.query(Payment).filter(Payment.payment_id == payment_id).first() 
    if payment :
        db.delete(payment)
        db.commit()
        return True
    print("Invalid payment_id.\nPlease enter a new one!")
    return None


#------------------------------------------------------------------------------------------------------------
#---------------------------------------------review crud----------------------------------------------------
#------------------------------------------------------------------------------------------------------------

def create_review(db: Session, comment: str, rating: int, review_date: date) :
    review = Review(comment= comment, rating= rating, review_date= review_date)
    if review :
        if not 0 <= rating <= 5 :
            print("\nError: rating must be between 0 and 5.")
            return None 
        db.add(review)
        db.commit()
        db.refresh(review) 
        return review

def retrieving_review(db: Session, review_id) :
    get_review = db.query(Review).filter(Review.review_id == review_id).all() 
    if get_review :
        return get_review 
    else :
        print("review_id doesn't exist!\nPlease enter a new review_id.") 
        return None 

def update_review(db: Session, review_id, attribute, new_value) :
    review = db.query(User).filter(Review.review_id == review_id).first()
    dict = ["comment", "rating", "review_date"]
    if review : 
        if attribute in dict :
            setattr(review, attribute, new_value) 
            db.commit()
            db.refresh(review) 
            return review 
        else :
            print("Attribute doesn't exist!\nPlease enter a new attribute.")
            return None 
    else :
        print("review_id doesn't exist!\nPlease enter a new review_id.") 
        return None 

def delete_review(db: Session, review_id) :
    review = db.query(Review).filter(Review.review_id == review_id).first() 
    if review :
        db.delete(review)
        db.commit()
        return True 
    print("Invalid review_id.\nPlease enter a new one!")
    return None

