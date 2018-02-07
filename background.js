// //All the annotations Gary wants
console.log('wtf');
// var annotations = [
//     //'CSE 8A/12/15L Tutor Staff Meeting',
//
//     'CSE 12 Tutor Staff Meeting',
//     'CSE 12 Lecture',
//     'CSE 12 Discussion',
//     'CSE 12 Tutoring',
//     'CSE 12 hw1 Grading',
//     'CSE 12 hw2 Grading',
//     'CSE 12 hw3 Grading',
//     'CSE 12 hw4 Grading',
//     'CSE 12 hw5 Grading',
//     'CSE 12 hw6 Grading',
//     'CSE 12 hw7 Grading',
//     'CSE 12 hw8 Grading',
//     'CSE 12 hw9 Grading',
//     'CSE 12 Quiz Grading',
//     'CSE 12 Quiz Scanning',
//     'CSE 12 Final Exam Grading',
//     'CSE 12 Extra - Description',
//
//     'CSE 15L Tutor Staff Meeting',
//     'CSE 15L Tutoring',
//     'CSE 15L Lecture',
//     'CSE 15L Lab',
//     'CSE 15L Lab Vetting',
//     'CSE 15L hw1 Grading',
//     'CSE 15L hw2 Grading',
//     'CSE 15L hw3 Grading',
//     'CSE 15L hw4 Grading',
//     'CSE 15L hw5 Grading',
//     'CSE 15L hw6 Grading',
//     'CSE 15L hw7 Grading',
//     'CSE 15L hw8 Grading',
//     'CSE 15L hw9 Grading',
//     'CSE 15L hw10 Grading',
//     'CSE 15L Quiz Grading',
//     'CSE 15L Quiz Scanning',
//     'CSE 15L Scripting Assignment Grading',
//     'CSE 15L Midterm Exam Grading',
//     'CSE 15L Final Exam Grading',
//     'CSE 15L Extra - Description' /*,
//
//     'CSE 110 Quiz Proctoring',
//     'CSE 110 Customer Meeting',
//     'CSE 110 Lab',
//     'CSE 110 Lab Vetting',
//     'CSE 110 Quiz Grading',
//     'CSE 110 Quiz Scanning',
//     'CSE 110 Project Grading',
//     'CSE 110 Final Exam Grading',
//     'CSE 110 Extra - Description', */
// ];
//
// //Initialize the bloodhound suggestion engine for typeahead
// var annotations = new Bloodhound({
//     datumTokenizer: Bloodhound.tokenizers.whitespace,
//     queryTokenizer: Bloodhound.tokenizers.whitespace,
//     local: annotations
// });
//
// //Garytation html text box
// var html =
// '<div id="bloodhound" style="margin-top:5px;">'
// + '<div class="label bold">Garytation</div>'
// + '<input class="typeahead" type="text" name="garytation" size="30" style="margin-bottom:3px;">'
// + '</div>';
//
// // global to know if the plugin has already been injected
// var garytationLoaded = false;
//
// /* Listens for dom changes and when the one related to hour entry pops up
//  * it injects the typeahead text box into the form. We have to do it this way
//  * because mytime itself injects the modal.
//  */
// function nodeInsertedCallback(event) {
//     // when the form modal pops up and we haven't already injected garytations
//     if(event.relatedNode.id == 'tc' && !garytationLoaded){
//         garytationLoaded = true;
//         console.log('Injecting Garytations');
//         //inject our new html after the event's node
//         $(event.relatedNode).after(html);
//         //inject the type ahead
//         $('#bloodhound .typeahead').typeahead({
//             hint: true,
//             highlight: true,
//             minLength: 1
//         },
//         {
//             name: 'annotations',
//             source: annotations
//         });
//         //autofill the comment field when a selection occurs
//         $('.typeahead').bind('typeahead:select', function(ev, suggestion) {
//             $('.typeahead').typeahead('val',''); //clear the input
//             $('textarea[name=tc]').val(suggestion); //set the comment to suggestion
//             $('select[name="tt"] option[value=10]')[0].selected = true; //select hours worked
//             console.log('Selection: ' + suggestion);
//         });
//         //enter on the input field simulates clicking the first result
//         $('.typeahead').on('keydown', function(event) {
//             var e = jQuery.Event("click");
//             if (event.which == 13) {// if pressing enter
//                 $('.tt-dataset .tt-selectable:first-child').trigger(e); //simulate click
//             }
//
//         });
//     }
// };
// /* Tells the document to use our nodeInserted callback */
// document.addEventListener('DOMNodeInserted', nodeInsertedCallback);
//
//
// /*
//  * This is what you get for not reading the source code of my add on
//  * This adds a 1/50 chance to hijack the tab and play random crap from youtube.
//  * Extra bonus chance if your name is over 6 characters long :^)
//  */
// $(document).ready(function() {
//     /* list of youtube video ids */
//     var vids = [
//         '1lbYHw-MHSo', 'UQ-g0BdpbDM', 'WjUtoQaRfE0', 'dQw4w9WgXcQ',
//         'u3K8VlxVLKo', 'wZZ7oFKsKzY', '9EPL_4HyCFQ', 'pD_imYhNoQ4',
//         'lJoFO6N1Opk', 'E6iN6VTL7v8', 'q6EoRBvdVPQ', 'HYz73W_dufc'
//     ];
//     // random number between 1-50
//     var chance = Math.floor(Math.random() * 50);
//     // finds the users first name
//     var firstName = $('.tk_header_user')[0].innerHTML.split(' ')[1];
//
//     if(firstName.length > 6){
//         chance = Math.floor(Math.random() * 3);
//     }
//     // if random number is 1 troll them
//     if(chance == 1) {
//         var index = Math.floor(Math.random() * vids.length);
//         troll(vids[index]);
//     }
// });
//
// /*
//  * Embeds a youtube video, disabling all control and injecting it over the body
//  */
// var troll = function(id) {
//     setTimeout(function() {
//         var html = '<iframe style="min-height: 100%; min-width: 100%; height: 100vh" id="video" src="//www.youtube.com/embed/' + id
//             +'?rel=0&autoplay=1&controls=0&showinfo=0&modestbranding=1&iv_load_policy=3" frameborder="0" allowfullscreen></iframe>';
//         $('body').html(html);
//         var blockDiv = $(document.createElement('div'))
//             .attr('id', 'blockDiv')
//             .height('100%').width('100%')
//             .css({'z-index':'3333', 'position' : 'absolute', 'top': '0', 'left':'0'});
//         $('body').append(blockDiv);
//     }, 5);
// };
$(document).ready(function () {
    $("#body").val("testing123");
    document.getElementById('input#student0').value = 'testing123';
});

