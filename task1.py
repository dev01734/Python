from datetime import datetime

class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.items = []
        self.comments = []  # Store comments

    def add_item(self, name, price, tax):
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }
        self.items.append(item)

    def calculate_total(self, discount):
        discount_factor = 1 - (discount / 100)  # Convert percentage to decimal
        total = 0
        for item in self.items:
            price = item["price"] * discount_factor  # Apply discount first
            tax = item["tax"]
            total += price + (price * tax)  # Then apply tax
        return total

    def add_comment(self, comment):
        """Adds a comment to the invoice."""
        self.comments.append(comment)

    def view_comments(self):
        """Returns a string representation of all comments."""
        if not self.comments:
            return "No comments available."
        return "\n".join(self.comments)

# Testing the Implementation
if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)
    
    invoice.add_comment("Client requested a 10% discount on equipment rental.")
    invoice.add_comment("Building cost adjusted due to material price hike.")
    
    invoice_total = invoice.calculate_total(20)
    print(f"Invoice Total: ${invoice_total:.2f}")
    print("\nInvoice Comments:")
    print(invoice.view_comments())
