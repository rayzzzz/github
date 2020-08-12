{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "url = 'http://www.taiwanlottery.com.tw/index_new.aspx'\n",
    "html = requests.get(url)\n",
    "sp = BeautifulSoup(html.text, 'html.parser')\n",
    "\n",
    "data = sp.find_all('div', {'class':'contents_box02'})\n",
    "date = data[0].find('span', {'class':'font_black15'})\n",
    "lottery = data[0].find_all('div', {'class':'ball_tx ball_green'})\n",
    "lottery.extend(data[0].find('div', {'class':'ball_red'}))\n",
    "lottery_len = len(lottery)\n",
    "\n",
    "\n",
    "\n",
    "print(\"威力彩期數: \" + date.text)\n",
    "print(\"開出順序: \", end='')\n",
    "for i in range(0, 6):\n",
    "    print(lottery[i].text, end='')\n",
    "print(\"\\n大小順序: \", end='')\n",
    "for i in range(6, 12):\n",
    "    print(lottery[i].text, end='')\n",
    "print(\"\\n第二區: \" + (lottery[len(lottery)-1]))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
