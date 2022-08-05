FROM justb4/jmeter as jmeter
RUN which java
RUN java -version
RUN pwd;ls -lrth
ARG Input_File
ARG Output_File
ARG project_id
ARG table_id
ARG projectname
ARG icmpno
ARG table_id_error

ENV Input_File		$Input_File
ENV Output_File     $Output_File
ENV project_id      $project_id
ENV table_id        $table_id
ENV projectname     $projectname
ENV icmpno          $icmpno
ENV table_id_error  $table_id_error

RUN echo $Input_File
RUN echo $Output_File
RUN echo $project_id
RUN echo $table_id
RUN echo $projectname
RUN echo $icmpno
RUN echo $table_id_error

CMD jmeter.sh -Jaggregate_rpt_pctl=95 -Jaggregate_rpt_pctl=99 -Jaggregate_rpt_pctl=99.9 -n -t ${Input_File} -l ${Output_File} -o dashboard
