-- отношение для хранения основных данных о книгах
create table books (
    id_book                         integer primary key autoincrement not null,
    book_name                       text not null,
    book_counter                    integer,
    book_author                     text,
    book_url                        text
);

-- отношение для хранения лог изменения цен на книги без авторизации
create table books_cost (
    id_scrap_cost                   integer primary key autoincrement not null
    id_book                         integer not null references books(id_book)
    cost_with_discount              integer,
    cost_without_discount           integer,
    cost_full                       integer,
    date_scrap_cost                 date
);

-- отношение для хранения лог изменения цен на книги после авторизации
create table books_cost_auth (
    id_scrap_cost_auth              integer primary key autoincrement not null,
    id_book_auth                    integer not null references books(id_book),
    cost_with_discount_auth         integer,
    cost_without_discount_auth      integer,
    cost_full_auth                  integer,
    date_scrap_cost_auth            date
);

-- отношение для хранения классов цен. позволяет сократить количество запросов к серверу сайта
create table class_cost (
    id_scrap_class                  integer primary key autoincrement not null,
    class_cost_with_discount        text,
    class_cost_without_discount     text,
    class_cost_full                 text,
    date_scrap_class                date
);

-- отношение для хранения списка разделов библиотеки
create table category (
    id_category                     integer primary key autoincrement not null,
    alpha_category                  text,
    true_name_category              text,
    slug_name_category              text
)