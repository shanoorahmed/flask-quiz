import click
from flask.cli import with_appcontext

from .extensions import db
from maths.models import User, Question

@click.command(name='create_db')
@with_appcontext
def create_db():
    db.create_all()
    q1 = Question(question_number=1, question_topic='Geometry', question_img=5672, question='ABC and DEF are two equilateral triangles with sides of 5.16cm each. Find the area of the shaded region. Round off the final answer to 2 decimal places.', answer='7.69')
    q2 = Question(question_number=2, question_topic='Lines and Angles', question_img=3880, question='Here, L1, L2, L3, L4 are four parallel lines and L5 is perpendicular to L1. Find the sum of squares of all the variables (e, h, i, k).', answer='20074')
    q3 = Question(question_number=3, question_topic='Time Speed Distance', question_img=0, question='Sasuke challenged Naruto to a running competition. Both of them run in a straight line towards a pole that is 65√3m long. There are 3 checkpoints on the ground between the starting line and the pole. The checkpoints make angles 30°, 45° and 60° with the top of the pole. The distance from the starting line to the first checkpoint is 60m. Both of them cross the first checkpoint in 3 sec. Between checkpoints, they run at a constant speed, but with every checkpoint, Sasuke and Naruto increase their speed instantly by 1m/s and 2m/s respectively. Find the sum of the total time taken by both of them to reach the pole from the first checkpoint. Round off the final answer to 2 decimal places.', answer='17.14')
    q4 = Question(question_number=4, question_topic='Ratio & Proportions', question_img=0, question='From a container of 150 L of Coca-Cola, 30 L of the soft drink is replaced with Pepsi. The process is repeated 10 times. Calculate the amount of Coca-Cola at the end of the process. Round off the final answer to 2 decimal places.', answer='16.11')
    q5 = Question(question_number=5, question_topic='Mensuration', question_img=0, question='A marshmallow has the shape of a cylinder with a diameter of 5cm and a height of 3cm. A dessert is made with 24 marshmallows, 2 stacked 3X4 array placed on a tray. Chocolate syrup exactly fills the gaps between marshmallows. What is the volume of the chocolate syrup used? (Skip the decimal part)', answer='193')
    q6 = Question(question_number=6, question_topic='Application of Derivatives', question_img=0, question='Consider a cylinder with height h, radius r and fixed volume V. What h/r ratio gives the minimum surface area?', answer='2')
    q7 = Question(question_number=7, question_topic='Matrices & Determinants', question_img=1630, question='If matrix M is given below and |adj(adj M)| = 18,74,161, then find x.', answer='7')
    q8 = Question(question_number=8, question_topic='Geometry', question_img=9961, question='Find the circle’s radius inscribed in two quarters. ACD and BDC are quarters of two circles having a radius of 1 cm.', answer='0.375')
    q9 = Question(question_number=9, question_topic='Geometry', question_img=1988, question='Inside the rectangle PQRS, there are right triangles PXS and QYR, as shown in the picture. Note that point Y is located along with SX. Length of PS = 25, PX = 7, QY = 15, and YS = 24. Find the length of PQ. (Skip the decimal part, if any)', answer='25')
    q10 = Question(question_number=10, question_topic='Approximations and Binomial Theorem', question_img=8616, question='If the below expression is approximately equal to A + Bx for small values of x, then find the value of A in decimal form.', answer='0.625')
    q11 = Question(question_number=11, question_topic='Permutation & Combination', question_img=0, question='Find the number of ways 3 girls and 5 boys can be seated around a circular table such that no two girls sit together and not more than two boys sit between two girls.', answer='720')
    q12 = Question(question_number=12, question_topic='Probability', question_img=0, question='Consider a function f: {1, 2, 3, ..., 13} -> {1, 2, 3, ..., 9}. Given that the function f is surjective and non-decreasing. The probability that f(7) = 4 is p/q where p and q are co-prime. Find the value of q.', answer='33')
    q13 = Question(question_number=13, question_topic='Inequalities', question_img=0, question='Let 1/x + 1/y + 1/z = 1 for x>0,y>0 and z>0. Find the minimum value of (x-1)(y-1)(z-1).', answer='8')
    q14 = Question(question_number=14, question_topic='Binomial Theorem and Sequence & Series', question_img=2765, question='Find the value of the below given expression:', answer='1')
    q15 = Question(question_number=15, question_topic='Geometry', question_img=3651, question='Four circles of equal size are inscribed in a square. Inside of the 4 circles is a smaller square tangent to each of the 4 circles. If the large square has a side length equal to 4, what is the area of the small square? (Answer up to two decimal points)', answer='0.68')
    q16 = Question(question_number=16, question_topic='Sequence & Series', question_img=6371, question='Given below expression, find ceil(x).', answer='1')
    q17 = Question(question_number=17, question_topic='Large Computation', question_img=0, question='A Prime Root Jutsu number is a positive integer whose all the prime factors are strictly less than its square root (e.g., 8 is the 1st prime jutsu number). Find the sum of the squares of the digits of the absolute difference of 28743569th and 17352991st prime root jutsu numbers.', answer='237')
    q18 = Question(question_number=18, question_topic='Large Computation', question_img=0, question='Let d(N, b) be the sum of the squares of the digits of the number N in base b. e.g. d(3,2) = 2, since 3 = 11(in base 2) and 1^2 + 1^2 = 2. Solve: d(8215385,8) * d(45593,4) + d(2254,2) * d(19082353,8).', answer='11064690737397577961')
    q19 = Question(question_number=19, question_topic='Matrices and Straight Line', question_img=0, question='A matrix ‘M’ describes the reflection of a point (x, y) about the line y=(2 - √3)x. The matrix ‘M’ also satisfies the relation AM – MA = I, where A is a nonsingular matrix. If A^(−1) is a symmetric matrix with entries x and y, then find |x-y|.', answer='2')
    q20 = Question(question_number=20, question_topic='Straight Line, Set Theory, Complex Number and Matrices', question_img=0, question='A point (x, y) undergoes the successive transformation about the lines y=x, y=0 and x=0. The initial and final points form a matrix ‘M’ such that trace(M) = 0. If z = x + iy is a complex number then find total number of elements in a set A which satisfy A = F ∩ G ∩ H, F = |adj(adj M)| = -1 where G = Im(z - 1/2) > 1, H = |Re(z – 2)| - Im(z) = 0', answer='1')
    db.session.add(q1)
    db.session.add(q2)
    db.session.add(q3)
    db.session.add(q4)
    db.session.add(q5)
    db.session.add(q6)
    db.session.add(q7)
    db.session.add(q8)
    db.session.add(q9)
    db.session.add(q10)
    db.session.add(q11)
    db.session.add(q12)
    db.session.add(q13)
    db.session.add(q14)
    db.session.add(q15)
    db.session.add(q16)
    db.session.add(q17)
    db.session.add(q18)
    db.session.add(q19)
    db.session.add(q20)
    db.session.commit()