DEFAULT_STUDENTS =  ('Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry')
SEED_MAP = {'V': 'Violets', 'C': 'Clover', 'G': 'Grass', 'R': 'Radishes'}

class Garden:

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        students = sorted(students)
        self.student_map = {}
        rows = diagram.split('\n')
        for i in range(len(rows[0])//2):
            plants = []
            index = i * 2
            for j in range(2):
                for seed in rows[j][index:index+2]:
                    plants.append(SEED_MAP[seed])
            self.student_map[students[i]] = plants
    
    def plants(self, student):
        return self.student_map[student]