from models import Product
from setup import session, Base, engine

Base.metadata.create_all(engine)

# --- Add ---
# product = Product(
#     name = "Pencil",
#     price = 0.52
# )
#
# session.add(product)
#
# product = Product(
#     name = "Notebook",
#     price = 1.31
# )
#
# session.add(product)
#
# product = Product(
#     name = "Eraser",
#     price = 0.72
# )
#
# session.add(product)
# session.commit()

# ---Query All---
products = session.query(Product).all()

for product in products:
    print(f"{product.name} - {product.price}")

# --- Update Price ---
update_product = session.query(Product).filter_by(name = "Pencil").first()
if update_product:
    update_product.price = 0.69
    session.commit()
    print("Product updated!")
else:
    print("Update failed")

# ---Query All---
products = session.query(Product).all()

for product in products:
    print(f"{product.name} - {product.price}")

# --- Delete ---

delete_product = session.query(Product).filter_by(name="Eraser").first()
if delete_product:
    session.delete(delete_product)
    session.commit()
    print("Product deleted.")
else:
    print("Product not found!")

# ---Query All---
products = session.query(Product).all()

for product in products:
    print(f"{product.name} - {product.price}")


