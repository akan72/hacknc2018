{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def parseLyrics(song): \n",
    "    word_list = song.split()\n",
    "    list_copy = word_list\n",
    "    for idx in range(len(word_list)):\n",
    "        word = word_list[idx]\n",
    "\n",
    "        #remove punctuation '?' and '.'\n",
    "        if word.find('?')!= -1:\n",
    "            word_list[idx] = word.replace(\"?\",\"\")\n",
    "        if word.find('.') != -1:\n",
    "            word_list[idx] = word.replace(\".\",\"\")\n",
    "        if word.find('\\n') != -1:\n",
    "            word_list[idx] = word.replace(\"\\n\",\"\")\n",
    "        if word.find('\\r') != -1:\n",
    "            word_list[idx] = word.replace(\"\\r\",\"\")\n",
    "\n",
    "    words_to_remove = []\n",
    "    for word in word_list:\n",
    "        #remove all part of song headers i.e. [Intro] or [Chorus]\n",
    "        if word.find('[') != -1:\n",
    "            words_to_remove.append(word)\n",
    "        elif word.find(']') != -1:\n",
    "            words_to_remove.append(word)\n",
    "\n",
    "    for word in words_to_remove:\n",
    "        word_list.remove(word)\n",
    "    word_set = set(word_list)\n",
    "\n",
    "    return word_set"
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
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
