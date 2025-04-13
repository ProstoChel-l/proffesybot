class UserState:

    def __init__(self):
        self.__ind = 0
        self.__nature = 0  # природа
        self.__tech = 0  # техника
        self.__sign = 0  # знаковая система
        self.__art = 0  # художественный образ
        self.__human = 0  # человек
        self.__user_answers = []

    @property
    def ind(self):
        return self.__ind

    @ind.setter
    def ind(self, ind):
        self.__ind = ind

    @property
    def nature(self):
        return self.__nature

    @nature.setter
    def nature(self, nature):
        self.__nature = nature

    @property
    def tech(self):
        return self.__tech

    @tech.setter
    def tech(self, tech):
        self.__tech = tech

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, sign):
        self.__sign = sign

    @property
    def art(self):
        return self.__art

    @art.setter
    def art(self, art):
        self.__art = art

    @property
    def human(self):
        return self.__human

    @human.setter
    def human(self, human):
        self.__human = human

    @property
    def user_answers(self):
        return self.__user_answers

    @user_answers.setter
    def user_answers(self, answer):
        self.__user_answers.append(answer)

    def user_answers_clear(self):
        self.__user_answers.clear()

    pass