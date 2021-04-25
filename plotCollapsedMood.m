function plotCollapsedMood(ratingCellArray, varargin)
%% Parse inputs
p = inputParser; p.KeepUnmatched = true;

p.addParameter('saveName', []);
p.addParameter('normalize', false, @islogical);
p.addParameter('doMonths', true, @islogical);
p.addParameter('startOnSunday', true, @islogical);


% Parse and check the parameters
p.parse(varargin{:});


%% Pad ratings for missed days
counter = 1;
for ii = ratingCellArray{1,1}:ratingCellArray{end,1}
    dates(counter) = ii;
    dateString = datestr(ii, 'yyyy-mm-dd');
    dateStringSplit = strsplit(dateString, '-');
    months(counter) = str2num(dateStringSplit{2});
    
    relevantIndex = find([ratingCellArray{:,1}] == ii);
    
    if ~isempty(relevantIndex)
        paddedRatings(counter) = ratingCellArray{relevantIndex,2};
    else
        paddedRatings(counter) = NaN;
    end
    
    counter = counter + 1;
    
end

if p.Results.normalize
    paddedRatings = (paddedRatings - nanmean(paddedRatings))./nanstd(paddedRatings);
end

if p.Results.startOnSunday
    startDay = weekday(dates(1));
    initialNans = startDay - 1;
    paddedRatings = [nan(1,initialNans), paddedRatings];
else
    initialNans = 0;
end

%% Do some plotting
% Reshape ratings into a 7xN size matrix where each column is a week
nWeeks = ceil(length(paddedRatings)/7);
paddedRatings(end+1:nWeeks*7) = NaN;
reshapedRatings = reshape(paddedRatings, [7,nWeeks]);

% Figure out where months are
if p.Results.doMonths
    monthTransitions = find(diff(months) == 1);
end

plotFig = figure; hold on;
imagesc(reshapedRatings, 'AlphaData',~isnan(reshapedRatings));
colorbar;
axisHandle = gca;
set(axisHandle,'TickLength',[0 0])
axisHandle.XTick = [];

if p.Results.doMonths
    xticksMonths = [];
    xtickLabelsMonths = {};
    priorColumn = 0;
    for ii = 1:length(monthTransitions)
        column = ceil(monthTransitions(ii)/7);
        row = monthTransitions(ii) - (column-1)*7;
        
        % horizontal line that divides month
        line([column-0.5, column+0.5], [row+0.5, row+0.5], 'Color', 'k');
        
        % right-sided line
        line([column+0.5, column+0.5], [0.5, row+0.5], 'Color', 'k');
        
        % left-sided line
        line([column-0.5, column-0.5], [row+0.5, 7.5], 'Color', 'k');
        xticksMonths = [xticksMonths, (priorColumn+column+0.5)/2];
        
        
        dateString = datestr(dates(monthTransitions(ii)-1), 'yyyy-mmmm-dd');
        dateStringSplit = strsplit(dateString, '-');
        
        
        xtickLabelsMonths = [xtickLabelsMonths, dateStringSplit{2}];
        
        priorColumn = column+0.5;
        
        
    end
    
    firstIndex = find(dates == ratingCellArray{1,1})+initialNans;
    column = ceil(firstIndex/7);
    row = firstIndex - (column-1)*7;
    
    % line before first date
    line([column-0.5, column+0.5], [row-0.5, row-0.5], 'Color', 'k');
    line([column-0.5, column-0.5], [row-0.5, 7.5], 'Color', 'k');
    line([column+0.5, column+0.5], [0.5, row-0.5], 'Color', 'k');
    bottomStartIndex = column+0.5;
    topStartIndex = column-0.5;
    
    endingIndex = find(dates == ratingCellArray{end,1})+initialNans;
    column = ceil(endingIndex/7);
    row = endingIndex - (column-1)*7;
    bottomEndIndex = column+0.5;
    topEndIndex = column-0.5;
    
    % line after last date
    line([column-0.5, column+0.5], [row+0.5, row+0.5], 'Color', 'k');
    line([column+0.5, column+0.5], [0.5, row+0.5], 'Color', 'k');
    line([column-0.5, column-0.5], [row+0.5, 7.5], 'Color', 'k');
    
    line([bottomStartIndex, bottomEndIndex], [0.5, 0.5], 'Color', 'k');
    line([topStartIndex, topEndIndex], [7.5, 7.5], 'Color', 'k');
    
    % get information for axes for the last month
    xticksMonths = [xticksMonths, (priorColumn+bottomEndIndex)/2];
    dateString = datestr(dates(end), 'yyyy-mmmm-dd');
    dateStringSplit = strsplit(dateString, '-');
    xtickLabelsMonths = [xtickLabelsMonths, dateStringSplit{2}];
    
    
end

% make the y axis labels
for ii = 1:7
    [~, dayOfWeek] = weekday(ratingCellArray{1,1}+ii-1-initialNans);
    yLabel{ii} = dayOfWeek;
end

axisHandle.YTick = 1:7;
axisHandle.YTickLabels = yLabel;
axisHandle.XTick = xticksMonths;
axisHandle.XTickLabels = xtickLabelsMonths;
axisHandle.DataAspectRatio = [1 1 1];
axisHandle.XTickLabelRotation = 45;
axisHandle.XLim = [0, bottomEndIndex+0.75];
axisHandle.YLim = [0 8];
set(gcf, 'Position', [46 303 1321 495]);

pause(1);
axisHandle.XAxis.Axle.Visible = 'off';
axisHandle.YAxis.Axle.Visible = 'off';


if ~isempty(p.Results.saveName)
    saveas(plotFig, p.Results.saveName);
end
end