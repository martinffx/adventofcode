(ns core.day1
  (:require [clojure.string :as s]))

(def arr (map #(Integer/parseInt %) (s/split (slurp "./src/1.1.txt") #"\n")))

(defn one []
  (reduce #(+ % %) 0 arr))

(defn two []
  (loop [i 0 dup (set []) freqs arr]
    (def freq (first freqs))
    (if (contains? dup i)
      (prn i)
      (recur (+ freq i) (conj dup i) (concat (rest freqs) [freq])))))
