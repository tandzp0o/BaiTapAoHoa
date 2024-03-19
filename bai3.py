from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btn1_click(self, **event_args):
    self.arr = [int(num.strip()) for num in self.txtNhap.text.split(',') if num.strip().isdigit()]
    # Lặp qua từng phần tử trong danh sách
    for i in range(1, len(self.arr)):
      key = self.arr[i]
      # Di chuyển các phần tử của danh sách đã được sắp xếp về phía trước
      # để tìm vị trí thích hợp cho phần tử hiện tại (key)
      j = i - 1
      while j >= 0 and key < self.arr[j]:
        self.arr[j + 1] = self.arr[j]
        j -= 1
      # Chèn phần tử vào vị trí đã tìm được
      self.arr[j + 1] = key
    for i in range(len(self.arr)):
      self.txtKQ.text += str(self.arr[i]) + ' '
    pass

  def txtNhap_change(self, **event_args):
    self.txtNhap.set_event_handler("change", self.txtNhap_change)
    pass

  def is_integer_sequence(self, input_str):
    # Tách chuỗi thành danh sách các phần tử
    elements = input_str.split(',')
    # Lặp qua từng phần tử để kiểm tra xem có phải là số nguyên không
    for element in elements:
        element = element.strip()  # Loại bỏ khoảng trắng xung quanh phần tử
        if not element.isdigit():
            return False
    return True



    
    
    
    


    
    
