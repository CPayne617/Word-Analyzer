text = """
The Boston Celtics will conclude a three-game homestand Sunday afternoon when they host the Eastern Conference rival Brooklyn Nets.

The Celtics have won four of their past five following Thursday's 120-107 win over Memphis. A 73-point second half paved the way to the victory.

On his 24th birthday, Jayson Tatum scored a team-leading 37 points -- including 21 in the fourth quarter -- and added five assists and six rebounds.

"(He's) much more vocal, and then on the court he's a bucket," Celtics coach Ime Udoka said on ESPN's NBA Today. "He can get 30 in his sleep. We've just tried to help him grow and expand his game. He's doing all the things he naturally does, but also becoming much more of a playmaker, a leader out there and getting everybody else involved."

The Celtics were missing star Jaylen Brown, but the right ankle sprain that he sustained in the first quarter of Tuesday's 107-98 win over Atlanta is not expected to be serious. Aaron Nesmith came out of Thursday's game with the same injury.

Memphis star Ja Morant scored 38 following back-to-back career performances, but 30 of his points came in the second half when the Celtics opened up a lead as large as 17 points on their way to the win.

"Defensively, I feel like we know who we are," said Al Horford, who had 21 points, 15 rebounds and five assists against the Grizzlies as part of his 12th double-double of the season. "On offense, I feel like we're continuing to find our identity and how we want to play and what we want to do. The more and more you start playing that way, it almost becomes second nature.

"We're not there yet, but I feel like we're making a lot of progress and it's going to be at the point that we're not even thinking about it and we're moving the ball, making the simple reads, and I feel like that's when we'll be at our best."

Against the Grizzlies, Marcus Smart also scored 18 and tied his career high with 12 assists.

Boston has a 2-1 season series lead entering its fourth and final game against Brooklyn. The 129-106 road win on Feb. 24 was its second consecutive against the Nets. Tatum scored 30 points to lead all scorers.

The Nets have lost three straight and five of their past six, but Kevin Durant returned to the court Thursday for a 113-107 loss to Miami. Durant, who had missed 21 games with a sprained left knee ligament, scored 31 points on 10-of-21 shooting. "I felt great," Durant said. "I'm only going to get better, more comfortable out there." "It was good to see him doing what he does best," Nets assistant coach Jacque Vaughn said of Durant's return.

Bruce Brown scored 21 points for the Nets, who were still playing without Kyrie Irving and Ben Simmons. Irving is expected to play against Boston; Simmons has yet to make his debut for Brooklyn since being acquired in a trade last month.

"It's going to be a work in progress, for sure, getting everybody up to speed, playing together," Vaughn said. "It's a puzzle that we're going to have to figure out together and do it in a timely fashion, so (it's) a great challenge."
"""

print(text.split())

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word]  = 1

print(word_count)