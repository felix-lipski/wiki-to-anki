import genanki
from scrape import html_to_dictionary, print_dictionary

style = ".hanzi { text-align:center; font-size:60px; } .latin { text-align:center; font-size:20px; }"

my_model = genanki.Model(
  4443778550,
  'Hanzi First',
  fields=[
    {'name': 'Hanzi'},
    {'name': 'Pinyin'},
    {'name': 'English'}
  ],
  templates=[
    {
      'name': 'Hanzi First Card',
      'qfmt': '<h1 class="hanzi">{{Hanzi}}<h1>',
      'afmt': """{{FrontSide}}<hr id="answer">
      <h3 class="latin">{{Pinyin}}<h1>
      <h3 class="latin">{{English}}<h1>""",
    },
    {
      'name': 'English First Card',
      'qfmt': '<h1 class="latin">{{English}}<h1>',
      'afmt': """{{FrontSide}}<hr id="answer">
      <h3 class="hanzi">{{Hanzi}}<h1>
      <h3 class="latin">{{Pinyin}}<h1>""",
    },
  ], css=style)

hanzi_first = genanki.Model(
  4443778558,
  'Hanzi First',
  fields=[
    {'name': 'QuestionHanzi'},
    {'name': 'AnswerPinyin'},
    {'name': 'AnswerEnglish'}
  ],
  templates=[
    {
      'name': 'Hanzi First Card',
      'qfmt': '<h1 class="hanzi">{{QuestionHanzi}}<h1>',
      'afmt': """{{FrontSide}}<hr id="answer">
      <h3 class="latin">{{AnswerPinyin}}<h1>
      <h3 class="latin">{{AnswerEnglish}}<h1>""",
    },
  ], css=style)

english_first = genanki.Model(
  4220784919,
  'English First',
  fields=[
    {'name': 'AnswerHanzi'},
    {'name': 'AnswerPinyin'},
    {'name': 'QuestionEnglish'}
  ],
  templates=[
    {
      'name': 'English First Card',
      'qfmt': '<h1 class="latin">{{QuestionEnglish}}<h1>',
      'afmt': """{{FrontSide}}<hr id="answer">
      <h3 class="hanzi">{{AnswerHanzi}}<h1>
      <h3 class="latin">{{AnswerPinyin}}<h1>""",
    },
  ], css=style)

# my_note = genanki.Note(model=hanzi_first, fields=['Capital of Argentina', 'Buenos Aires'])

my_deck = genanki.Deck(
  8997934782,
  'Mandarin 1 - 1000')

# my_deck.add_note(genanki.Note(model=english_first, fields=['国民党', 'guómíndǎng', 'Kuomintang, Nationalist Party, Kuomintang (KMT)']))
# my_deck.add_note(genanki.Note(model=english_first, fields=['消费者', 'xiāofèizhě', 'customer, buyer, consumer']))
# my_deck.add_note(genanki.Note(model=english_first, fields=['消费者', 'xiāofèizhě', 'customer, buyer, consumer']))
# my_deck.add_note(my_note)


if __name__ == "__main__":
    wiki1 = open("H:/Projects/Python/anki01/wiki1.html", "r", encoding="utf8").read()
    dict1 = html_to_dictionary(wiki1)
    for word in dict1:
        # my_deck.add_note(genanki.Note(model=hanzi_first,    fields=[word["hanzi"], word["pinyin"], word["english"]]))
        # my_deck.add_note(genanki.Note(model=english_first,  fields=[word["hanzi"], word["pinyin"], word["english"]]))
        my_deck.add_note(genanki.Note(model=my_model, fields=[word["hanzi"], word["pinyin"], word["english"]]))
    
    genanki.Package(my_deck).write_to_file('mandarin1.apkg')
    # print_dictionary(dict1)