ALTER TABLE users
  ADD banned integer not null default 0 check(banned >= 0 and banned <= 1);