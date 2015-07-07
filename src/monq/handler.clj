(ns monq.handler
  (:require [compojure.core :refer :all]
            [compojure.route :as route]
            [ring.middleware.defaults :refer [wrap-defaults site-defaults]]))

(defn positions []
  "positions"
  )

(defn create-position [proto]
  "create-position"
  )

(defn get-position [id]
  "get-position"
  )

(defn update-position [id proto]
  "update-position"
  )

(defn delete-position [id]
  "delete-position"
  )

(defroutes app-routes
  (context "/positions" []
           (defroutes positions-routes
             (GET "/" [] (positions))
             (POST "/" {body :body} (create-position body))
             (context "/:id" [id]
                      (GET "/" [] (get-position id))
                      (PUT "/" {body :body} (update-position id body))
                      (DELETE "/" [] (delete-position id))
                      )
             )
           )
  (route/not-found "Not Found"))

(def app
  (wrap-defaults app-routes (assoc site-defaults :security false)))