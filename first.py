class Student:

  def __init__(self, full_name, group, grades=None):
    self.full_name = full_name
    self.group = group
    self.grades = grades if grades is not None else []

  def add_grade(self, grade):
    if not (isinstance(grade, int) and 2 <= grade <= 5):
      raise ValueError("Только целлые числа от 2 до 5")
    self.grades.append(grade)

  def average(self):
    if not self.grades:
      return None
    return sum(self.grades) / len(self.grades)

  def is_excellent(self):
    avg = self.average()
    if avg is None:
      return False
    return avg >= 4.5 and all(grade >= 4 for grade in self.grades)


if __name__ == "__main__":
  student1 = Student("bleeh", "random group1")
  student2 = Student("bleeh2", "random group2")

  student1.add_grade(5)
  student1.add_grade(4)
  student1.add_grade(5)

  student2.add_grade(5)
  student2.add_grade(5)
  student2.add_grade(5)
  student2.add_grade(4)

  print(f"Студент: {student1.full_name}, Группа: {student1.group}")
  print(f"Средний балл: {student1.average()}")
  print(f"Отличник: {student1.is_excellent()}\n")

  print(f"Студент: {student2.full_name}, Группа: {student2.group}")
  print(f"Средний балл: {student2.average()}")
  print(f"Шикарно!!: {student2.is_excellent()}")