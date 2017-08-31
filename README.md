# MiniReadability

I've found some interesting task in the internet, and complied it in python
Description:
Console application, geting URL as parameter. It gets useful information from web page, formate it for comfortable reading: 
  -max line length 80 simbols, if more - carry by words
  -insert empty line between paragraphs
  -insert URL text from links in square brackets
Information shoud be saved in text file. File name shoud be generated automaticaly from URL like this: 
http://lenta.ru/news/2013/03/dtp/index.html=>  [CUR_DIR]/lenta.ru/news/2013/03/dtp/index.txt


Большинство веб-страниц сейчас перегружено всевозможной рекламой...Наша задача «вытащить» из веб-страницы только полезную информацию, отбросив весь «мусор» (навигацию, рекламу и тд).

Полученный  текст  нужно  отформатировать  для максимально комфортного чтения  в  любом текстовом  редакторе.  Правила  форматирования:  ширина  строки  не  больше  80  символов  (если больше,  переносим  по  словам),  абзацы  и  заголовки  отбиваются  пустой  строкой. Если  в  тексте встречаются ссылки, то URL вставить в текст в квадратных скобках. Остальные правила на ваше усмотрение.

Программа  оформляется  в  виде утилиты командной  строки,  которой  в качестве  параметра указывается произвольный URL. Она  извлекает  по  этому URL страницу, обрабатывает  ее  и формирует текстовый файл с текстом статьи, представленной на данной странице.

В качестве примера можно взять любую статью на lenta.ru, gazeta.ru и тд 

Алгоритм должен быть максимально универсальным, то есть работать на большинстве сайтов. Усложнение задачи 1: Имя  выходного  файла  должно  формироваться автоматически  по URL. Примерно так: http://lenta.ru/news/2013/03/dtp/index.html=>  [CUR_DIR]/lenta.ru/news/2013/03/dtp/index.txt
