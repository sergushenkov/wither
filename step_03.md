Map - карта местности, содержит характеристики ячеек (стена, провал, дорога, заросли, вход) и их содержимое в этот момент времени (вещи, монстры, ведьмак)

Player - игрок, содержит характеристики игрока (здоровье, уровень манны, инвентарь, активные доспех и оружие). Методы: подобрать предмет, сменить оружие или доспех, атаковать монстра, использовать знак, изменить здоровье. Уровень манны постепенно восстанавливается.

Monster - монстр, содержит характеристики монстра (здоровье, состояние - бродит, атакует, убегает, в засаде, под контролем, спит). Методы: атаковать, следующее действие (остаться на месте, атаковать, куда переместиться). 

Разные подклассы монстров - имеют разный базовый уровень здоровья, урон, стойкость к разным типам урона, модель поведения (определяет следующее действие) 

Armor - доспех. Характеристики - вес, прочность, снижаемый урон. В надетом состоянии уменьшает наносимый игроку урон, теряя при этом прочность. Когда прочность уменьшается до нуля - становится бесполезным

Weapon - оружие. Характеристики - вес, урон, радиус поражения (ближний, дальний), тип урона (режущий, колющий, рубящий)

Potion - зелье. Восстанавливает уровень здоровья игрока

Bag - мешок - список оружия, доспехов, зелий, которые сейчас при себе у игрока (не активны). Имеет ограничение по весу (условно 1 доспех + 3 оружия + 5 зелий). Методы - сделать доспех/оружие активным, выкинуть из мешка. Вещи с пола автоматически подбираются (если доступно по весу)

Signs - знаки - список доступных мгновенных заклинаний, расходуют манну
- аард - удар на расстоянии
- аксий - контроль монстра (атакует других монстров, не трогает игрока)
- игни - поджечь
- ирден - зафиксировать монстра
- квен - защита от атаки монстра
- сомн - усыпить монстра
