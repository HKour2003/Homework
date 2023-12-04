'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array  A[]  of n   integers each separated by a space.

Constraints   2<=n<=10,   -100<=A[i]<=100   Output Format

Print the runner-up score.'''

if __name__ == '__main__':
    n = int(input())
    if 2 <= n <= 10:
        scores = list(map(int, input().split()))
        if all(-100 <= score <= 100 for score in scores):
            sorted_scores = sorted(set(scores), reverse=True)
            runner_up_score = sorted_scores[1]
            print(runner_up_score)
        else:
            print()
    else:
        print()

