#возможность добавлять юниту оружие и доспехи. Это потребует отдельного класса отвечающего
#за объект амуниции. Одевание на юнита обьекта амуниции производит пересчет характеристик юнита ()
import random

class Armor:
    def __init__(self, name, attack, defence):
        if all([
            isinstance(name, str),
            isinstance(attack, int),
            isinstance(defence, int),
        ]):
            if all([
                attack >= 0,
                defence >= 0
            ]):
                self.name = name
                self.attack = attack
                self.defence = defence
            else:
                raise ValueError
        else:
            raise ValueError


sword = Armor('sword', 33, 0)
mace = Armor('mace', 10, 0)
pistol = Armor('pistol', 5, 0)
slingshot = Armor('slingshot', 1, 0)

shield = Armor('shield', 0, 5)
helmet = Armor('helmet', 0, 3)
socks = Armor('socks', 0, 2)


class Unit:
    def __init__(self, name, health, attack, defence):
        if all([
            isinstance(name, str),
            isinstance(health, int),
            isinstance(attack, int),
            isinstance(defence, int)
        ]):
            if all([
                health >= 0,
                attack >= 0,
                defence >= 0
            ]):
                self.name = name
                self.health = health
                self.attack = attack
                self.defence = defence
            else:
                raise ValueError
        else:
            raise ValueError

    def health_getter(self):
        return self._health
    def health_setter(self, health):
        self._health = health if 0 <= health <= 100 else 0
    health = property(health_getter, health_setter)

    def attack_getter(self):
        return self._attack
    def attack_setter(self, attack):
        if attack >= 100: print('Cheater')
        self._attack = attack if attack >= 0 else 0
    attack = property(attack_getter, attack_setter)


    def defence_getter(self):
        return self._defence
    def defence_setter(self, defence):
        self._defence = defence if defence >= 0 else 0
    defence = property(defence_getter, defence_setter)


    def damage(self, protiv):
        damage = self.attack - protiv.defence
        if damage > 0:
            protiv.health = protiv.health - damage

            print(f'{self.name}  atacked {protiv.name}  leave health {protiv.health} ')
        else:
            print(f'{self.name} dont atack {protiv.name} with health {protiv.health}')
        return self


    def __add__(self, other):
        if isinstance(other, Armor):
            self.attack = other.attack + self.attack
            self.defence = other.defence + self.defence
            return self
        else:
            raise TypeError

pers = Unit('Cherv', 100, 10, 1)
pers2 = Unit('Akula', 100, 14, 1)

pers = pers + slingshot + socks
pers2 = pers2 + pistol +  socks

# print(pers.damage(pers2))
# print(pers2.damage(pers))

#создайте класс Битва, который принимает два юнита и реализует механику битвы -
# юниты поочередно атакуют друг-друга пока у одного из них не здоровье не станет 0
#
class Combat():

    def __init__(self, first, second):
        if not isinstance(first, Unit): raise TypeError
        if not isinstance(second, Unit): raise TypeError
        self.first = first
        self.second = second

    def battle(self):
        t = 0
        list = (self.first, self.second)
        re = random.choice(list)

        while not self.first.health == 0 or self.second.health == 0:
            if re == self.first:
                self.first.damage(self.second)
                self.second.damage(self.first)
            elif re == self.second:
                self.second.damage(self.first)
                self.first.damage(self.second)
            t += 1
        return f'numbers of the battles {t}'

k = Combat(pers, pers2)
print(k.battle())
