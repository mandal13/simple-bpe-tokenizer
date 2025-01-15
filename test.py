from tokenizer import BaseTokenizer
from tokenizer import BasicTokenizer
from tokenizer import AdvanceTokenizer

# Test the tokenizers
tokenizer1 = BaseTokenizer()
encoded = tokenizer1.encode("Hello, World!")
decoded = tokenizer1.decode(encoded)
print(encoded)  # Byte-level token IDs
print(decoded)  # Original text

text = """
Taylor Alison Swift (born December 13, 1989) is an American singer-songwriter. Known for her autobiographical songwriting, artistic reinventions, and cultural impact, Swift is a leading figure in popular music and the subject of widespread media coverage.

Swift signed to Big Machine Records in 2005, debuting as a country singer with the albums Taylor Swift (2006) and Fearless (2008). The singles "Teardrops on My Guitar", "Love Story", and "You Belong with Me" found crossover success on country and pop radio formats. She incorporated rock on Speak Now (2010) and electronic on Red (2012), later re-calibrating her image from country to pop with the synth-pop set 1989 (2014); the ensuing media scrutiny inspired the hip-hop-imbued Reputation (2017). The albums contained the Billboard Hot 100 number-one singles "We Are Never Ever Getting Back Together", "Shake It Off", "Blank Space", "Bad Blood" and "Look What You Made Me Do".

Shifting to Republic Records in 2018, Swift released the electropop album Lover (2019) and switched to indie folk styles in the 2020 albums Folklore and Evermore. She experimented with subdued pop genres on Midnights (2022) and The Tortured Poets Department (2024), and began re-recording her Big Machine albums as Taylor's Version[a] due to an ownership dispute with the label. Through the 2020s, she garnered the US number one songs "Cardigan", "Willow", "All Too Well", "Anti-Hero", "Cruel Summer", "Is It Over Now?", and "Fortnight". She has undertaken six concert tours, including the Eras Tour (2023–2024), the highest-grossing tour of all time. Her films include Miss Americana (2020), All Too Well: The Short Film (2021), and The Eras Tour (2023)—the highest-grossing concert film.

Swift is one of the world's best-selling music artists, with a record seven albums that moved one million copies first-week. She is the highest-grossing touring artist, the first billionaire from music primarily, and the world's richest female musician. She has been listed amongst history's greatest artists by publications such as Rolling Stone, Billboard and Forbes, as well as the only individual from the arts to have been named the Time Person of the Year (2023). Amongst her accolades are 14 Grammy Awards (including a record four Album of the Year wins), a Primetime Emmy Award, and a record four IFPI Global Recording Artist of the Year awards. Swift is the most-awarded artist of the American Music Awards (40), the Billboard Music Awards (49), and the MTV Video Music Awards (30). She is an advocate of artists' rights and women's empowerment. Her fans are known as Swifties.

Life and career
Early life
Taylor Alison Swift was born on December 13, 1989, in West Reading, Pennsylvania.[1] She is named after the singer-songwriter James Taylor.[2][3] Her father, Scott Kingsley Swift, was a stockbroker for Merrill Lynch, and her mother, Andrea Gardner Swift (née Finlay), worked as a mutual fund marketing executive.[4] Swift's younger brother, Austin, is an actor.[5] Their maternal grandmother, Marjorie Finlay (née Moehlenkamp), was an opera singer,[6] whose singing in church became one of Swift's earliest memories of music that shaped her career.[4] Swift is of Scottish, English, and German descent, with distant Italian and Irish ancestry.[7][8][9]

Swift spent her early years on a Christmas tree farm in Pennsylvania that her father had purchased from one of his clients,[10] and she spent her summers at her family's vacation home in Stone Harbor, New Jersey, where she occasionally performed acoustic songs at a local coffee shop.[11] She is Christian[12] and attended preschool and kindergarten at a Montessori school run by the Bernardine Sisters of St. Francis before transferring to the Wyndcroft School.[13][14] When her family moved to Wyomissing, she attended Wyomissing Area Junior/Senior High School.[15][16] As a child, she performed in Berks Youth Theatre Academy productions[17] and traveled regularly to New York City for vocal and acting lessons.[18] Her early love for country music was influenced by Shania Twain, Patsy Cline, LeAnn Rimes, and the Dixie Chicks,[14] and she spent weekends performing at local festivals and events.[19][20] After watching a documentary about Faith Hill, she became determined to pursue a country-music career in Nashville, Tennessee.[21]

At 11, Swift traveled to Nashville with her mother to visit record labels and submit demo tapes of Dolly Parton and Dixie Chicks karaoke covers.[22] She was rejected by all the labels, which led her to focus on songwriting.[23] She started learning the guitar at 12 with the help of Ronnie Cremer, a computer repairman and local musician who also assisted Swift with writing an original song.[24] In 2003, Swift and her parents started working with the talent manager Dan Dymtrow. With his help, Swift modeled for Abercrombie & Fitch and had an original song included on a Maybelline compilation CD.[25] After performing original songs at an RCA Records showcase, 13-year-old Swift was given an artist development deal and began to travel regularly to Nashville with her mother.[26][27] To help Swift break into the country music scene, her father transferred to Merrill Lynch's Nashville office when she was 14 years old, and the family relocated to Hendersonville, Tennessee.[28][29] Swift attended Hendersonville High School[30] before transferring to Aaron Academy after two years, which better accommodated her touring schedule through homeschooling. She graduated one year early.[3][31]

2004–2008: Career beginnings and first album
In Nashville, Swift worked with experienced Music Row songwriters such as Troy Verges, Brett Beavers, Brett James, Mac McAnally, and the Warren Brothers[32][33] and formed a lasting working relationship with Liz Rose.[34] They began meeting for two-hour writing sessions every Tuesday afternoon after school.[35] Rose called the sessions "some of the easiest I've ever done. Basically, I was just her editor. She'd write about what happened in school that day. She had such a clear vision of what she was trying to say. And she'd come in with the most incredible hooks." At 14, Swift became the youngest artist signed by Sony/ATV Tree Music Publishing.[36] She left RCA Records due to the label's lack of care and them "cut[ting] other people's stuff". She was also concerned that development deals can shelve artists[27][20] and recalled: "I genuinely felt that I was running out of time. I wanted to capture these years of my life on an album while they still represented what I was going through.
"""

tokenizer2 = BasicTokenizer()
tokenizer2.train(text, 512)
encoded = tokenizer2.encode("December 13, 1989, ")
decoded = tokenizer2.decode(encoded)
print(encoded)  # Word-level token IDs
print(decoded)  # Original text

tokenizer3 = AdvanceTokenizer()
tokenizer3.train(text, 512)
encoded = tokenizer3.encode("December 13, 1989, ")
decoded = tokenizer3.decode(encoded)
print(encoded)  # Subword-level token IDs
print(decoded)  # Original text
