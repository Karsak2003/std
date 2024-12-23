"""
Реализовать иерархию классов, описывающих разные виды объектов одного
типа (например, сервоприводов (синхронный/асинхронный/линейный и
т.п.). Реализовать минимум 3 уровня иерархии. Реализовать возможность
задания характеристик (например, для двигателя это угол поворота, скорость
вращения, ускорение и т.п.). Реализовать строковое представление классов
«магическими» методами  __str__() и  __repr__(), быть готовым пояснить
различия этих методов. Перегрузить условные операторы (см. магические
методы  __eq__(),  __ne__(),  __lt__(),  __gt__(),  __le__(),  __ge__()) для
реализации возможности сравнения экземпляров класса.
"""

#//import random


class Weapon():
    def __init__(self, 
            Damage:float         = 1., 
            AttackSpeed:float    = 1., 
            AttackRange:float    = 1., 
            CriticalChange:float = .5, 
            CriticalDamage:float = .5
        ):
        self._baseDamage:float              = Damage
        self._besaAttackSpeed:float         = AttackSpeed
        self._baseAttackRange:float         = AttackRange
        self._baseCriticalChange:float      = CriticalChange
        self._AddCriticalMultiplier:float   = CriticalDamage
    
    def Get_AttackDamage(self) -> float:
        return self._baseDamage
    
    def Get_CriticalDamage(self) -> float:
        return self._baseDamage * (1 + self._AddCriticalMultiplier)
    
    def Get_DPS(self) -> float:
        """DPS ~ D*AS + D*ACM*AS*CD = D*AS*(1 + ACM*CD)
        Returns:
            float: _description_
        """
        step1:float = self._baseDamage * self._besaAttackSpeed
        step3:float =  self._AddCriticalMultiplier * self._baseCriticalChange
        return step1 * (1 + step3)    
    

class MeleeWeapon(Weapon):
    def __init__(self, 
            Damage = 1, 
            AttackSpeed = 1, 
            AttackRange = 1, 
            CriticalChange = 0.5, 
            CriticalDamage = 0.5
        ):
        super().__init__(Damage, AttackSpeed, AttackRange, CriticalChange, CriticalDamage)
    
class Sword(MeleeWeapon):
    def __init__(self, 
            Damage = 1, 
            AttackSpeed = 1, 
            AttackRange = 1, 
            CriticalChange = 0.5, 
            CriticalDamage = 0.5
        ):
        super().__init__(Damage, AttackSpeed, AttackRange, CriticalChange, CriticalDamage)
    
    

    


