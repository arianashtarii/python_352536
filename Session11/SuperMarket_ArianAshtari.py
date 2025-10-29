import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json


class ProductManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("سیستم مدیریت محصولات")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        self.products = []
        self.filename = "products.json"

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # عنوان اصلی
        title_label = tk.Label(self.root, text="🛍️ سیستم مدیریت محصولات",
                               font=('Arial', 18, 'bold'),
                               bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=10)

        # فریم ورودی داده
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10, padx=20, fill='x')

        # ورودی نام محصول
        tk.Label(input_frame, text="نام محصول (30-35 کاراکتر):",
                 bg='#f0f0f0', font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=5)
        self.name_entry = tk.Entry(input_frame, width=40, font=('Arial', 10))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # نمایش طول نام
        self.name_length_label = tk.Label(input_frame, text="طول: 0",
                                          bg='#f0f0f0', fg='#666', font=('Arial', 9))
        self.name_length_label.grid(row=0, column=2, padx=5)
        self.name_entry.bind('<KeyRelease>', self.update_name_length)

        # ورودی قیمت
        tk.Label(input_frame, text="قیمت:", bg='#f0f0f0', font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=5)
        self.price_entry = tk.Entry(input_frame, width=20, font=('Arial', 10))
        self.price_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # ورودی تعداد
        tk.Label(input_frame, text="تعداد:", bg='#f0f0f0', font=('Arial', 10)).grid(row=2, column=0, sticky='w', pady=5)
        self.quantity_entry = tk.Entry(input_frame, width=20, font=('Arial', 10))
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        # دکمه‌های عملیات
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="➕ افزودن محصول", command=self.add_product,
                  bg='#27ae60', fg='white', font=('Arial', 10, 'bold'), width=15).grid(row=0, column=0, padx=5)

        tk.Button(button_frame, text="👁️ نمایش همه", command=self.show_all,
                  bg='#3498db', fg='white', font=('Arial', 10, 'bold'), width=15).grid(row=0, column=1, padx=5)

        tk.Button(button_frame, text="💾 ذخیره", command=self.save_to_file,
                  bg='#f39c12', fg='white', font=('Arial', 10, 'bold'), width=15).grid(row=0, column=2, padx=5)

        tk.Button(button_frame, text="📂 بارگذاری", command=self.load_from_file,
                  bg='#9b59b6', fg='white', font=('Arial', 10, 'bold'), width=15).grid(row=0, column=3, padx=5)

        tk.Button(button_frame, text="📊 آمار", command=self.show_stats,
                  bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'), width=15).grid(row=0, column=4, padx=5)

        # جستجو
        search_frame = tk.Frame(self.root, bg='#f0f0f0')
        search_frame.pack(pady=10, padx=20, fill='x')

        tk.Label(search_frame, text="🔍 جستجو:", bg='#f0f0f0', font=('Arial', 10)).grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, width=30, font=('Arial', 10))
        self.search_entry.grid(row=0, column=1, padx=5)
        tk.Button(search_frame, text="جستجو", command=self.search_product,
                  bg='#2c3e50', fg='white', font=('Arial', 9)).grid(row=0, column=2, padx=5)

        # ناحیه نمایش نتایج
        self.result_text = scrolledtext.ScrolledText(self.root, width=80, height=20,
                                                     font=('Arial', 10), bg='white', fg='#2c3e50')
        self.result_text.pack(pady=10, padx=20, fill='both', expand=True)

        # وضعیت
        self.status_label = tk.Label(self.root, text="آماده", bg='#f0f0f0',
                                     font=('Arial', 9), fg='#666')
        self.status_label.pack(side='bottom', pady=5)

    def update_name_length(self, event=None):
        length = len(self.name_entry.get())
        self.name_length_label.config(text=f"طول: {length}")
        if 30 <= length <= 35:
            self.name_length_label.config(fg='green')
        else:
            self.name_length_label.config(fg='red')

    def add_product(self):
        name = self.name_entry.get().strip()
        price = self.price_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        # اعتبارسنجی
        if not name:
            messagebox.showerror("خطا", "لطفاً نام محصول را وارد کنید")
            return

        if len(name) < 30 or len(name) > 35:
            messagebox.showerror("خطا", "نام محصول باید بین 30 تا 35 کاراکتر باشد")
            return

        for char in name:
            if not (char.isalnum() or char.isspace()):
                messagebox.showerror("خطا", "نام فقط می‌تواند شامل حروف، اعداد و فاصله باشد")
                return

        try:
            price = float(price)
            if price < 0:
                messagebox.showerror("خطا", "قیمت نمی‌تواند منفی باشد")
                return
        except:
            messagebox.showerror("خطا", "قیمت باید عدد باشد")
            return

        try:
            quantity = int(quantity)
            if quantity < 0:
                messagebox.showerror("خطا", "تعداد نمی‌تواند منفی باشد")
                return
        except:
            messagebox.showerror("خطا", "تعداد باید عدد صحیح باشد")
            return

        # اضافه کردن محصول
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)

        # پاک کردن فیلدها
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        self.update_status(f"✅ محصول '{name}' اضافه شد")
        messagebox.showinfo("موفق", "محصول با موفقیت اضافه شد")

    def show_all(self):
        self.result_text.delete(1.0, tk.END)

        if not self.products:
            self.result_text.insert(tk.END, "📭 هیچ محصولی وجود ندارد\n")
            return

        total_value = 0
        self.result_text.insert(tk.END, "📦 لیست همه محصولات:\n")
        self.result_text.insert(tk.END, "=" * 60 + "\n")

        for i, product in enumerate(self.products, 1):
            value = product['price'] * product['quantity']
            total_value += value
            self.result_text.insert(tk.END,
                                    f"{i}. {product['name']}\n"
                                    f"   💰 قیمت: {product['price']} | 📦 تعداد: {product['quantity']} | 🏷️ ارزش: {value}\n"
                                    f"{'-' * 40}\n")

        self.result_text.insert(tk.END, f"\n💰 ارزش کل موجودی: {total_value}\n")
        self.update_status(f"📊 نمایش {len(self.products)} محصول")

    def save_to_file(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.products, f, ensure_ascii=False, indent=2)
            self.update_status(f"💾 {len(self.products)} محصول ذخیره شد")
            messagebox.showinfo("موفق", "داده‌ها با موفقیت ذخیره شد")
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در ذخیره فایل: {e}")

    def load_from_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.products = json.load(f)
            self.update_status(f"📂 {len(self.products)} محصول بارگذاری شد")
            messagebox.showinfo("موفق", "داده‌ها با موفقیت بارگذاری شد")
        except:
            messagebox.showerror("خطا", "فایل وجود ندارد یا خطا در خواندن")

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.products = json.load(f)
            self.update_status(f"📂 {len(self.products)} محصول بارگذاری شد")
        except:
            pass

    def show_stats(self):
        self.result_text.delete(1.0, tk.END)

        total_products = len(self.products)
        total_quantity = sum(p['quantity'] for p in self.products)
        total_value = sum(p['price'] * p['quantity'] for p in self.products)

        self.result_text.insert(tk.END, "📊 آمار محصولات:\n")
        self.result_text.insert(tk.END, "=" * 40 + "\n")
        self.result_text.insert(tk.END, f"📦 تعداد محصولات: {total_products}\n")
        self.result_text.insert(tk.END, f"🔢 تعداد کل آیتم‌ها: {total_quantity}\n")
        self.result_text.insert(tk.END, f"💰 ارزش کل موجودی: {total_value}\n")

        if self.products:
            avg_price = sum(p['price'] for p in self.products) / total_products
            self.result_text.insert(tk.END, f"📈 میانگین قیمت: {avg_price:.2f}\n")

        self.update_status("📊 آمار نمایش داده شد")

    def search_product(self):
        search_term = self.search_entry.get().strip().lower()
        if not search_term:
            messagebox.showwarning("هشدار", "لطفاً عبارت جستجو را وارد کنید")
            return

        found_products = [p for p in self.products if search_term in p['name'].lower()]

        self.result_text.delete(1.0, tk.END)

        if found_products:
            self.result_text.insert(tk.END, f"🔍 {len(found_products)} محصول یافت شد:\n")
            self.result_text.insert(tk.END, "=" * 50 + "\n")

            for i, product in enumerate(found_products, 1):
                value = product['price'] * product['quantity']
                self.result_text.insert(tk.END,
                                        f"{i}. {product['name']}\n"
                                        f"   💰 قیمت: {product['price']} | 📦 تعداد: {product['quantity']}\n"
                                        f"   🏷️ ارزش: {value}\n"
                                        f"{'-' * 30}\n")
        else:
            self.result_text.insert(tk.END, "❌ هیچ محصولی یافت نشد\n")

        self.update_status(f"🔍 جستجو برای '{search_term}' - {len(found_products)} نتیجه")

    def update_status(self, message):
        self.status_label.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductManagerGUI(root)
    root.mainloop()