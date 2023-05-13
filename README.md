# Fin_math
В этом репозитории собраны примеры базовых финансовых расчетов.

|**№**|**Название.**|**Стек.**|**Описание.**|**Ключевые слова.**|
|:-:|:-----------------------:|:---:|:-----------------------------------:|:------------:|
|01.|[Опционный калькулятор](https://github.com/medvedev-gs/Fin_math/blob/91f08601ee8bafca404aba9d5925383cf8083a4c/01.%20%D0%9E%D0%BF%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B8%CC%86%20%D0%BA%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80/Options_calculator_2.ipynb)|Numpy, SciPy, Matplotlib, Seaborn|Применение формулы Блека - Шоулза для оценки теоретической стоимости и "греков" опциона. Графические представления профиля прибыли / убытков на дату экспирации, изменения теоретической стоимости и "греков" опциона в зависимости от различных факторов.|Блек - Шоулз|
|02.|[Проверка логарифмированных доходностей на нармальность распределения](https://github.com/medvedev-gs/Fin_math/blob/ae488d2490eb0f7415a91a8504b953187d203198/02.%20%D0%9B%D0%BE%D0%B3%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B4%D0%BD%D0%B5%D0%B2%D0%BD%D0%BE%D0%B8%CC%86%20%D0%B4%D0%BE%D1%85%D0%BE%D0%B4%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%84%D1%8C%D1%8E%D1%87%D0%B5%D1%80%D1%81%D0%B0/%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D0%BC%20%D0%B4%D0%BD%D0%B5%D0%B2%D0%BD%D1%83%D1%8E%20%D0%BB%D0%BE%D0%B3%D0%B0%D1%80%D0%B8%D1%84%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%83%D1%8E%20%D0%B4%D0%BE%D1%85%D0%BE%D0%B4%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%84%D1%8C%D1%8E%D1%87%D0%B5%D1%80%D1%81%D0%B0%20%D0%BD%D0%B0%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%20%D0%A0%D0%A2%D0%A1%20%D0%BD%D0%B0%20%D0%BD%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F.ipynb)|Statsmodels, Pandas, Numpy, SciPy, Matplotlib, Seaborn|Тестирование гипотезы о следовании логарифмированных доходностей финансового актива нормальному распределению с применением QQ-plot, теста Шапиро - Уилка.|Тестирование гипотез, Шапиро - Уилк, QQ - plot|
|03.|[Расчет подразумеваеых и реализованных волатильностей](https://github.com/medvedev-gs/Fin_math/blob/596435cd8d6cfedbaac8897663d84af5ca9799c6/03.%20%D0%9D%D0%B0%D1%81%D1%87%D0%B5%D1%82%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85%20%D0%B8%20%D0%BF%D0%BE%D0%B4%D1%80%D0%B0%D0%B7%D1%83%D0%BC%D0%B5%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D1%85%20%D0%B2%D0%BE%D0%BB%D0%B0%D1%82%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B5%D0%B8%CC%86/%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%B8%20%D0%BF%D0%BE%D0%B4%D1%80%D0%B0%D0%B7%D1%83%D0%BC%D0%B5%D0%B2%D0%B0%D0%B5%D0%BC%D0%B0%D1%8F%20%D0%B2%D0%BE%D0%BB%D0%B0%D1%82%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C.ipynb)|Pandas, Numpy, SciPy, Matplotlib, Seaborn|Прикладные методы ООП в финансовом моделировании. Применение пользовательских функций и классов для автоматизации процессов парсинга данных, обработки, финансовых расчетов. Прикладное применение теории ценообразования опционов. Моделирование процессов изменения реализованной и подразумеваемой волатильностей.|ООП, Блек - Шоулз, реализованная волатильность, подразумеваемая волатильность, арбитраж волатильностей.|
|04.|[Расчет бета - коэффициента акции](https://github.com/medvedev-gs/Fin_math/blob/51dd1390af8dedcb4eb72f681db5de35c0f78301/04.%20%D0%91%D0%B5%D1%82%D0%B0%20-%20%D0%BA%D0%BE%D1%8D%D1%84%D1%84%D0%B8%D1%86%D0%B8%D0%B5%D0%BD%D1%82%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B8/%D0%A0%D0%B0%D1%81%D1%87%D0%B5%D1%82%20%D0%B1%D0%B5%D1%82%D0%B0%20-%20%D0%BA%D0%BE%D1%8D%D1%84%D1%84%D0%B8%D1%86%D0%B8%D0%B5%D0%BD%D1%82%D0%B0%20%D0%B0%D0%BA%D1%86%D0%B8%D0%B8.ipynb)|Pandas, Matplotlib, Seaborn, Sklearn|Пример расчета одного из показателей, применяемых в управлении портфелем методами языка Python и его библиотек. Применение линейной регрессии в целях оценки статистических метрик предположительно связанных случайных процессов.|Финансовый менеджмент, управление портфелем, бета - коэффициент, линейная регрессия.|
|05.|[CAPM - модель](https://github.com/medvedev-gs/Fin_math/blob/90cb04705c3d60dde3c1d3db1eedfedd62299434/05.%20CAPM%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C/CAPM%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C.ipynb)|Pandas, Matplotlib, Seaborn|С применением бета - коэффициента, рассчитанного в предыдущем разделе найдем ожидаемую доходность акции. Используем CAPM - модель.|Финансовый менеджмент, CAPM - модель, оценка доходности.|
|06.|[Коэффициент Шарпа](https://github.com/medvedev-gs/Fin_math/blob/bdfa1b6c419cb89b7663224cb6136fb65a45e43e/06.%20%D0%9A%D0%BE%D1%8D%D1%84%D1%84%D0%B8%D1%86%D0%B8%D0%B5%D0%BD%D1%82%20%D0%A8%D0%B0%D1%80%D0%BF%D0%B0/%D0%9A-%D1%82%20%D0%A8%D0%B0%D1%80%D0%BF%D0%B0%20(%D1%80%D0%B0%D1%81%D1%87%D0%B5%D1%82).ipynb)|Numpy, Pandas, Matplotlib, Seaborn|Наряду с бета - коэффициентом, к-т Шарпа является еще одной метрикой, позволяющей сравнить между собой различные инвестиционные альтернативы. Приводим методику расчета и сравнения между собой акций и индексного портфеля.|Финансовый менеджмент, к-т Шарпа.|
|07.|[Расчет показателя value at risk](https://github.com/medvedev-gs/Fin_math/blob/139eb9771fbc7c66da484137d622a41455a8efe9/07.%20VaR%20(value%20at%20risk)/Value%20-%20at%20-%20risk.ipynb)|Numpy, Pandas, SciPy, Matplotlib, Seaborn|Приводим методику расчета метрики рыночного риска с применением нескольких подходов и пример практичекого применения.|Риск - менеджмент, Value at risk.|