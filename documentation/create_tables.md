# Tietokannan CREATE TABLE-lauseet

```
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(64) NOT NULL,
        email VARCHAR(64) NOT NULL,
        username VARCHAR(16) NOT NULL,
        password VARCHAR(128) NOT NULL,
        remember BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        CHECK (remember IN (0, 1))
);
CREATE UNIQUE INDEX ix_account_username ON account (username);

CREATE TABLE project (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(128) NOT NULL,
        description VARCHAR(1024) NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        running BOOLEAN NOT NULL,
        owner_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (running IN (0, 1)),
        FOREIGN KEY(owner_id) REFERENCES account (id)
);

CREATE TABLE participation (
        project_id INTEGER,
        account_id INTEGER,
        FOREIGN KEY(project_id) REFERENCES project (id) ON DELETE CASCADE,
        FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
);

CREATE TABLE workload (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        date DATE NOT NULL,
        hours INTEGER NOT NULL,
        task VARCHAR(128) NOT NULL,
        worker_id INTEGER NOT NULL,
        project_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(worker_id) REFERENCES account (id),
        FOREIGN KEY(project_id) REFERENCES project (id)
);
```