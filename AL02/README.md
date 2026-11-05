# AL02-Shared
# Writeup from Garrett Hickie

# Monday Tasks:

1. - 5. Executed within main.py

6. Briefly identify worst-case scan growth, index-build growth, and the expected average-case growth of one lookup in an existing index.

    Worst-case Scan Growth: The requested ID is the last record (B4) or is not in the catalog, so every record must be checked. This is an O(n) check.

    Index-Build Growth: To build the index, each book record must be processed once. This is O(n), increasing linearly as the list increases. 

    Expected Average-Case Growth (one lookup): The requested ID is somewhere in the middle, so only some of the records are examined before a match is found. As long as the index already exists, this is O(1). 

# Tuesday Tasks:

1. Inspect first_id, all_ids, ordered_pairs, and halving_sizes in growth_examples.py. Use the catalog records for the first three; the halving example takes a size.

    first_id: B1
    all_ids: ['B1', 'B2', 'B3', 'B4']
    ordered_pairs: [('B1', 'B1'), ('B1', 'B2'), ('B1', 'B3'), ('B1', 'B4'), ('B2', 'B1'), ('B2', 'B2'), ('B2', 'B3'), ('B2', 'B4'), ('B3', 'B1'), ('B3', 'B2'), ('B3', 'B3'), ('B3', 'B4'), ('B4', 'B1'), ('B4', 'B2'), ('B4', 'B3'), ('B4', 'B4')]
    halving_sizes(8): [8, 4, 2, 1]

2. For each, record a Big-O label and one short reason in your README.

    First ID: O(1) constant
    Reason: Returns the first record directly without scanning the catalog.

    All IDs: O(n) linear
    Reason: Visits each record once to collect all IDs. 

    Ordered Pairs: O(n^2) quadratic
    Reason: Uses nested loops to create ordered pairs.

    Halving Sizes: O(log n)
    Reason: Repeatedly halves at every step.

3. Explain why a request for B1 stops sooner than a request for B4 or an absent ID in this catalog order. Connect that observation to best/worst cases.

    B1 is at the top of the catalog, and our functions naturally draw from the beginning of said catalog. A request for B4 requires examining multiple records before finding a match. An absent ID requires checking every record before determining that the book is not present.

4. - 5. Executed within main.py

# Thursday Tasks:

1. Recommend an approach for a patron’s one B1 lookup when the catalog list is already available and no index has been built. Give a short reason.

    Recommended approach: Scan lookup

    Reason: If the catalog list is already available and only one lookup is needed, scanning the list is simpler because no index needs to be built first. For a single request, the overhead of building an index is unnecessary.

2. Recommend an approach for a circulation desk’s many repeated catalog-ID requests when it can retain an index. Give a short reason.

    Recommended approach: Indexed Lookup

    Reason: When many requests are expected, building an index once allows the same index to be reused for future lookups. This avoids repeatedly scanning the entire catalog.


3. Explain the work to build that index, its additional storage, and why reusing it differs from rebuilding it for every request. No new feature is required.

    Building the index requires one pass through all catalog records, which is O(n) work.

    The index uses additional storage because it stores a dictionary entry for each book ID and its associated record.

    Reusing an existing index differs from rebuilding it each time because the setup work is performed only once. After the index has been created, many lookups can use the same index. Rebuilding the index for every request would repeat the same O(n) setup cost over and over again.  

4. - 6. Executed within main.py

# AI Usage Statement:

The only AI I used this week was on Thursday when comparing our created main.py to Cash's commented main2.py demo that included the queried index function. I was trying to differentiate what the queries added that ours was lacking. At first, I was worried our code wasn't retaining our index and we would have to refactor a bit. However, Copilot helped me come to the realization that the queries allowed for multiple ID requests to be input at once within the same function, although it did parse them individually. Ty and I decided our code didn't require that feature to move forward with the assignment, so we used it as a point of reference. 