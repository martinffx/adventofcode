(ns core.day2
  (:require [clojure.string :as s]
            [clojure.data :as d]))

(def arr (s/split (slurp "./src/2.txt") #"\n"))

(defn count-values
  [val values]
  (if (= 0 (count (filter
                   #(= (% 1) val)
                   values)))
    0 1))

(defn a []
  (loop [twice 0 thrice 0 ids arr]
    (if (empty? ids)
      (do
        (* twice thrice))
      (do
        (def id-map (reduce (fn [c x]
                              (if (contains? c x)
                                (conj c [x (+ (c x) 1)])
                                (conj c [x 1]))) {} (first ids)))
        (recur (+ twice (count-values 2 id-map))
               (+ thrice (count-values 3 id-map))
               (rest ids))))))

(defn compare-vals [val values]
  (loop [x (first values) y values]
    (when (not-empty y)
      (def dif (d/diff val x))
      (if (= 1 (count (filter identity (dif 0))))
        (dif 2)
        (recur (first y) (rest y))))))

(defn b []
  (def v-arr (map #(vec %) arr))
  (loop [val (first arr) values v-arr]
    (if-let [dif (compare-vals val v-arr)]
      (s/join (filter identity dif))
      (recur (first (rest values)) (rest values)))))
