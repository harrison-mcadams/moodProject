function analyzeByDayOfWeek(ratingsCellArray, varargin)
%% collect some inputs
p = inputParser; p.KeepUnmatched = true;

p.addParameter('saveName', []);

% Parse and check the parameters
p.parse(varargin{:});

%% Get the data
daysOfTheWeek = weekday([ratingsCellArray{:,1}]);

sundays = find(daysOfTheWeek == 1);
sundayRatings = [ratingsCellArray{sundays,2}];

mondays = find(daysOfTheWeek == 2);
mondayRatings = [ratingsCellArray{mondays,2}];

tuesdays = find(daysOfTheWeek == 3);
tuesdayRatings = [ratingsCellArray{tuesdays,2}];

wednesdays = find(daysOfTheWeek == 4);
wednesdayRatings = [ratingsCellArray{wednesdays,2}];

thursdays = find(daysOfTheWeek == 5);
thursdayRatings = [ratingsCellArray{thursdays,2}];

fridays = find(daysOfTheWeek == 6);
fridayRatings = [ratingsCellArray{fridays,2}];

saturdays = find(daysOfTheWeek == 7);
saturdayRatings = [ratingsCellArray{saturdays,2}];


%% Do the plotting
data = nan(length({ratingsCellArray{:,1}}),7);
data(1:length(sundayRatings),1) = sundayRatings;
data(1:length(mondayRatings),2) = mondayRatings;
data(1:length(tuesdayRatings),3) = tuesdayRatings;
data(1:length(wednesdayRatings),4) = wednesdayRatings;
data(1:length(thursdayRatings),5) = thursdayRatings;
data(1:length(fridayRatings),6) = fridayRatings;
data(1:length(saturdayRatings),7) = saturdayRatings;

plotFig = figure;
h1 = subplot(2,1, 1);
set(h1, 'OuterPosition', [0,0.5, 1, .4]);
plotSpread_scatter(data, 'spreadWidth', 0.8, 'distributionMarker', '.', 'markerSize', 1000, 'alpha', 0.2);
hold on;
boxplot(data, 'Labels',{'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'});
hold on;
%plot(1:7, [mean(sundayRatings), mean(mondayRatings), mean(tuesdayRatings), mean(wednesdayRatings), mean(thursdayRatings), mean(fridayRatings), mean(saturdayRatings)], 'Color', 'k');
ylabel('Mood Rating')

h2 = subplot(2,1, 2);
set(h2, 'OuterPosition', [0,0.3, 1, .2]);
ax = imagesc([mean(sundayRatings), mean(mondayRatings), mean(tuesdayRatings), mean(wednesdayRatings), mean(thursdayRatings), mean(fridayRatings), mean(saturdayRatings)]);
axis = gca;
set(axis,'TickLength',[0 0])
ylabel('Mean')
axis.XTick = [];
axis.YTick = [];

if ~isempty(p.Results.saveName)
    saveas(plotFig, p.Results.saveName);
end



end