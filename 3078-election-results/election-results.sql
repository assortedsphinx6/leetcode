WITH voter_counts AS (
    SELECT voter, COUNT(candidate) AS choices
    FROM Votes
    WHERE candidate IS NOT NULL
    GROUP BY voter
),
candidate_votes AS (
    SELECT v.candidate, SUM(1.0 / vc.choices) AS total_votes
    FROM Votes v
    JOIN voter_counts vc
      ON v.voter = vc.voter
    WHERE v.candidate IS NOT NULL
    GROUP BY v.candidate
)
SELECT candidate
FROM candidate_votes
WHERE total_votes = (SELECT MAX(total_votes) FROM candidate_votes)
ORDER BY candidate;
