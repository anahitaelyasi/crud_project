#define your tables
from sqlalchemy import Column, Integer, String, Numeric, CheckConstraint, ForeignKey, Date, PrimaryKeyConstraint, Text, func
from db import Base


class User(Base) :

    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    name = Column(String) 
    email = Column(String)
    phone_number = Column(Numeric)
    password = Column(String) 
    role = Column(String) 

    __table_args__ = (
        CheckConstraint("role IN ('guest','crews','manager')", name= 'valid_role'),
    )


class Hotel(Base) :

    __tablename__ = 'hotel'

    hotel_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True) 
    location = Column(String(200))
    name = Column(String(100))
    rating = Column(Numeric(2, 1))


class Room(Base) :

    __tablename__ = 'room'

    room_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey("hotel.hotel_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False) 
    room_type = Column(String)
    room_number = Column(Numeric)
    status = Column(String(20))
    max_guests = Column(Integer)
    price_per_night = Column(Numeric(10, 2)) 

    __table_args__ = (
        CheckConstraint("room_type IN ('single','double','suite')", name='valid_room_type'), 
        CheckConstraint("status IN ('available','reserved','out of service')", name='valid_room_status')  
    )


class Reservation(Base) :

    __tablename__ = "reservation"

    reservation_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True) 
    user_id = Column(Integer, ForeignKey("user.user_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False)
    room_id = Column(Integer, ForeignKey("room.room_id", ondelete="CASCADE"), onupdate= "CASCADE", nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotel.hotel_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False)
    number_of_guests = Column(Integer)
    checkIn_date = Column(Date)
    checkOut_date = Column(Date) 

class Reserve_Room(Base) :

    __tablename__ = "reserve_room"

    reservation_id = Column(Integer, ForeignKey("reservation.reservation_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False)
    room_id = Column(Integer, ForeignKey("room.room_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False) 

    __table_args__ = (
        PrimaryKeyConstraint('reservation_id', 'room_id'),
    ) 


class Reserve_Hotel(Base) :

    __tablename__ = "reserve_hotel"

    reservation_id = Column(Integer, ForeignKey("reservation.reservation_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotel.hotel_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('reservation_id', 'hotel_id'),
    )


class Discount(Base) :

    __tablename__ = "discount"

    discount_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    status = Column(String)
    discount_percentage = Column(Integer)
    code = Column(String(20), unique=True)

    __table_args__ = (
        CheckConstraint("discount_percentage >= 0 AND discount_percentage <= 100", name='valid_discount_range'), 
        CheckConstraint("status IN ('active','expired')", name='valid_discount_status')      
    )


class Payment(Base) :

    __tablename__ = "payment"

    payment_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True) 
    reservation_id = Column(Integer, ForeignKey("reservation.reservation_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False)
    payment_methods = Column(String)
    payment_status = Column(String(20)) 
    payment_date = Column(Date) 
    payment_amount = Column(Numeric(10, 2)) 

    __table_args__ = (
        CheckConstraint("payment_methods IN ('cash','online')", name='valid_methods'),
        CheckConstraint("payment_status IN ('Paid', 'Cancelled', 'Pending')", name='valid_status')
    )


class Review(Base) :

    __tablename__ = "review"

    review_id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotel.hotel_id", ondelete="CASCADE", onupdate= "CASCADE"), nullable=False) 
    comment = Column(Text)
    rating = Column(Integer)
    review_date = Column(Date, default=func.current_date()) 

    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name='valid_review_rating'),
    )

