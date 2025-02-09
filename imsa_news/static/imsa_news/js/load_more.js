// $(document).ready(function() {
//     var start = 5;  // Количество новостей, которое будет подгружаться
//     var loading = false;  // Флаг для предотвращения нескольких запросов одновременно

//     $('#load-more-btn').click(function(e) {
//         e.preventDefault();
        
//         if (loading) return;  // Если уже идет загрузка, ничего не делаем
        
//         loading = true;
//         $(this).text('Загружаем...');

//         // AJAX-запрос
//         $.ajax({
//             url: '/load-more-news/',  // Путь к обработчику
//             data: {
//                 'start': start  // Параметр для определения с какого места загружать данные
//             },
//             success: function(response) {
//                 if (response.news) {
//                     // Добавляем новые новости в контейнер
//                     var newNews = '';
//                     $.each(response.news, function(index, item) {
//                         newNews += '<div class="news-item">' +
//                                        '<a href="' + item.link + '" target="_blank" class="news-link">' +
//                                            '<img src="' + item.image + '" alt="Image" class="news-image">' +
//                                        '</a>' +
//                                        '<div class="news-text">' +
//                                            '<p class="news-title"><a href="' + item.link + '" class="news-link">' + item.title + '</a></p>';
//                         if (item.heading3) newNews += '<p class="news-heading3">' + item.heading3 + '</p>';
//                         if (item.heading2) newNews += '<p class="news-heading2">' + item.heading2 + '</p>';
//                         if (item.pading) newNews += '<p class="news-pading">' + item.pading + '</p>';
//                         if (item.author) newNews += '<p class="news-author">Автор: <a href="' + item.author_link + '" target="_blank">' + item.author + '</a></p>';
//                         newNews += '</div></div>';
//                     });
                    
//                     // Добавляем новые новости в контейнер
//                     $('#news-container').append(newNews);
//                     start += 5;  // Обновляем start для загрузки следующей партии новостей
//                 }

//                 // Если новостей больше нет
//                 if (!response.more_news) {
//                     $('#load-more-btn').hide();  // Скрываем кнопку, если новостей больше нет
//                 }
                
//                 // Восстанавливаем текст кнопки
//                 loading = false;
//                 $('#load-more-btn').text('More Posts');
//             }
//         });
//     });
// });
