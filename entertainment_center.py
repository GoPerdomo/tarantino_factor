import tarantino_factor
import media

reservoir_dogs = media.Movie("Reservoir Dogs", "(1992)",
                             "After a simple jewelry heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.",
                             "https://upload.wikimedia.org/wikipedia/en/f/f6/Reservoir_dogs_ver1.jpg",
                             "https://www.youtube.com/watch?v=vayksn4Y93A")

pulp_fiction = media.Movie("Pulp Fiction", "(1994)",
                           "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

jackie_brown = media.Movie("Jackie Brown", "(1997)",
                           "A middle-aged woman finds herself in the middle of a huge conflict that will either make her a profit or cost her life.",
                           "https://upload.wikimedia.org/wikipedia/en/8/80/Jackie_Brown70%27s.jpg",
                           "https://www.youtube.com/watch?v=G7HkBDNZV7s")

kill_bill_1 = media.Movie("Kill Bill: Volume 1", "(2003)",
                          "The Bride wakens from a four-year coma. Now she must wreak vengeance on the team of assassins who betrayed her - a team she was once part of.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                          "https://www.youtube.com/watch?v=LPLNjDDqVvY")

kill_bill_2 = media.Movie("Kill Bill: Volume 2", "(2004)",
                          "The Bride continues her quest of vengeance against her former boss and lover Bill, the reclusive bouncer Budd and the treacherous, one-eyed Elle.",
                          "https://upload.wikimedia.org/wikipedia/en/4/46/Kill_bill_vol_two_ver.jpg",
                          "https://www.youtube.com/watch?v=TnSTPTs_RiA")

death_proof = media.Movie("Death Proof", "(2007)",
                          'Two separate sets of women are stalked at different times by a scarred stuntman who uses his "death proof" cars to execute his murderous plans.',
                          "https://upload.wikimedia.org/wikipedia/en/b/b4/Death_Proof_USA_Poster.png",
                          "https://www.youtube.com/watch?v=QABR2sE0jXc")

inglourious_basterds = media.Movie("Inglourious Basterds", "(2009)",
                                   "In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same.",
                                   "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                                   "https://www.youtube.com/watch?v=KnrRy6kSFF0")

django_unchained = media.Movie("Django Unchained", "(2012)",
                               "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
                               "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")

hateful_eight = media.Movie("The Hateful Eight", "(2015)",
                            "In the dead of a Wyoming winter, a bounty hunter and his prisoner find shelter in a cabin currently inhabited by a collection of nefarious characters.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d4/The_Hateful_Eight.jpg",
                            "https://www.youtube.com/watch?v=6_UI1GzaWv0")


movies = [reservoir_dogs, pulp_fiction, jackie_brown, kill_bill_1, kill_bill_2, death_proof, inglourious_basterds, django_unchained, hateful_eight]
tarantino_factor.open_movies_page(movies)
