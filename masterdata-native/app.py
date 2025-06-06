from flask import Flask, request, render_template, redirect, url_for
from models import db, Car, Customer, Rental, Brand, Employee  # ganti 'product' jadi 'Car'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    cars = Car.query.all()  # perbaiki dari 'product'
    customers = Customer.query.all()
    rentals = Rental.query.all()
    brands = Brand.query.all()
    employees = Employee.query.all()
    return render_template('index.html',
        cars=cars,
        customers=customers,
        rentals=rentals,
        brands=brands,
        employees=employees
    )

@app.route('/cars')
def car_list():
    cars = Car.query.all()
    return render_template('cars.html', cars=cars)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    new_customer = Customer(
        name=request.form['name'],
        phone=request.form['phone']
    )
    db.session.add(new_customer)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_rental', methods=['POST'])
def add_rental():
    new_rental = Rental(
        car_id=int(request.form['car_id']),
        customer_id=int(request.form['customer_id']),
        employee_id=int(request.form['employee_id']),
        start_date=request.form['start_date'],
        end_date=request.form['end_date']
    )
    db.session.add(new_rental)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_brand', methods=['POST'])
def add_brand():
    new_brand = Brand(name=request.form['name'])
    db.session.add(new_brand)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_employee', methods=['POST'])
def add_employee():
    new_employee = Employee(name=request.form['name'], position=request.form['position'])
    db.session.add(new_employee)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
