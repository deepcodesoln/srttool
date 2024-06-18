"""A spaCy-like JSON example of what might be emitted by the Ginza tool."""

SIMPLE_GINZA_SPACY_JSON = r"""[
 {
  "paragraphs": [
   {
    "raw": "俺はもう一度 中国に行くぜ",
    "sentences": [
     {
      "tokens": [
       {"id":1,"orth":"俺","tag":"代名詞","pos":"PRON","lemma":"俺","norm":"俺","head":6,"dep":"nsubj","ner":"O"},
       {"id":2,"orth":"は","tag":"助詞-係助詞","pos":"ADP","lemma":"は","norm":"は","head":-1,"dep":"case","ner":"O"},
       {"id":3,"orth":"もう","tag":"副詞","pos":"ADV","lemma":"もう","norm":"もう","head":1,"dep":"advmod","ner":"O"},
       {"id":4,"orth":"一度","tag":"名詞-普通名詞-副詞可能","pos":"NOUN","lemma":"一度","norm":"一度","head":3,"dep":"obl","ner":"B-Frequency","whitespacce":" "},
       {"id":5,"orth":"中国","tag":"名詞-固有名詞-地名-国","pos":"PROPN","lemma":"中国","norm":"中国","head":2,"dep":"obl","ner":"B-Country"},
       {"id":6,"orth":"に","tag":"助詞-格助詞","pos":"ADP","lemma":"に","norm":"に","head":-1,"dep":"case","ner":"O"},
       {"id":7,"orth":"行く","tag":"動詞-非自立可能","pos":"VERB","lemma":"行く","norm":"行く","head":0,"dep":"ROOT","ner":"O"},
       {"id":8,"orth":"ぜ","tag":"助詞-終助詞","pos":"PART","lemma":"ぜ","norm":"ぜ","head":-1,"dep":"mark","ner":"O"}
      ]
     }
    ]
   }
  ]
 },
 {
  "paragraphs": [
   {
    "raw": "てめえ  俺は",
    "sentences": [
     {
      "tokens": [
       {"id":1,"orth":"てめえ","tag":"代名詞","pos":"PRON","lemma":"てめえ","norm":"てまえ","head":2,"dep":"nmod","ner":"O","whitespacce":" "},
       {"id":2,"orth":" ","tag":"空白","pos":"NOUN","lemma":" ","norm":" ","head":-1,"dep":"dep","ner":"O"},
       {"id":3,"orth":"俺","tag":"代名詞","pos":"PRON","lemma":"俺","norm":"俺","head":0,"dep":"ROOT","ner":"O"},
       {"id":4,"orth":"は","tag":"助詞-係助詞","pos":"ADP","lemma":"は","norm":"は","head":-1,"dep":"case","ner":"O"}
      ]
     }
    ]
   }
  ]
 }
]
"""
