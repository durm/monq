(ns monq.dbspec
  (:require [clojure.java.jdbc :as sql])
  )

(def db {:classname "com.mysql.jdbc.Driver" ; must be in classpath
         :subprotocol "mysql"
         :subname "//localhost:3306/monq"
         ; Any additional keys are passed to the driver
         ; as driver-specific properties.
         :user "monqu21"
         :password "monqp22"})

(defn create-positions-table []
  (sql/create-table-ddl
    :positions
    [:id :int "PRIMARY KEY" "GENERATED ALWAYS AS IDENTITY"]
    [:full_title "text"]
    [:short_title "text"]
    [:desc "text"]
    [:bg_image "varchar(255)"]
    [:image "varchar(255)"]
    [:created_at :timestamp "NOT NULL" "DEFAULT CURRENT_TIMESTAMP"]
    [:updated_at :timestamp "NOT NULL" "DEFAULT CURRENT_TIMESTAMP" "ON UPDATE CURRENT_TIMESTAMP"]
    )
  )

(defn drop-positions-table []
  (sql/drop-table-ddl :positions)
  )